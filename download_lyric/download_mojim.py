'''
author: openopentw(YJC)
description: to download & parse the lyrics on the mojim webpage & return the parsed lyrics
usage:
    1. import the file
    2. use the function "main_get_lyric()" to get lyric
'''

import google
import urllib
from urllib import request
import lxml.html
import re

# google for "{artist} {song} 歌詞 site:mojim.com"
def google_lyric(artist, song, DEBUG=False):
    '''
    DEBUG: print log messages or not
    return: urls which might contains the lyrics
    '''
    # make query words
    query = ' '.join([artist, song, '歌詞', 'site:mojim.com'])
    if DEBUG == True:
        print('Quering "{}" on Google ...'.format(query))
    # get the first 5 hits in Google
    urls = []
    for url in google.search(query, stop=10):
        urls += [url]
    return urls

# download HTML CODE from url & PARSE TREE
def get_html_tree(url, DEBUG=False):
    '''
    DEBUG: print log messages or not
    return: a file tree which is parsed from url given
    '''
    if DEBUG == True:
        print('getting data from: {}'.format(url))
    h = {'User-Agent':'Mozilla/5.0'}
    response = request.Request(url, headers=h)
    data = request.urlopen(response).read().decode('utf-8')
    tree = lxml.html.fromstring( data )
    return tree

# parse artist & song & lyrics from html tree
def parse_artist_song_lyric(tree, DEBUG=False):
    '''
    DEBUG: print log messages or not
    return: a file tree which is parsed from url given
    return: artist, song, plain_lyric, dynamic_lyric
            and if DEBUG is specified, it will return the whole lyric additionally
    '''
    # artist
    node_artist = tree.xpath('//dl[@id="fsZx1"]')[0]
    artist = node_artist.text.replace('\n', '').replace('\r', '')
    # artist = ''.join(artist.splitlines())

    # song
    node_song = node_artist.xpath('dt')[0]
    song = node_song.text
    song = re.sub('^ ', '', song)

    # lyric
    node_lyric = node_artist.xpath('dd')[0]
    for br in node_lyric.xpath('br'):   # add '\n' before <br>
        br.tail = '\n' + br.tail if br.tail else '\n'
    lyric = node_lyric.text_content().replace('更多更詳盡歌詞 在 ※ Mojim.com　魔鏡歌詞網 \n', '')

    # plain lyric
    # plain_lyric = ''.join(re.findall('(?!\[.*\n)', lyric))
    plain_lyric = song + '\n' + artist
    for line in lyric.splitlines():
        if not re.match('(\[.*)', line):
            plain_lyric += '\n' + line

    # dynamic lyric
    dynamic_lyric = ''.join(re.findall('\[\d\d:\d\d\.\d\d].*\n', lyric))

    if DEBUG == True:
        return (artist, song, plain_lyric, dynamic_lyric, lyric)
    return (artist, song, plain_lyric, dynamic_lyric)

# the main function
def main_get_lyric(artist, song, DEBUG=False):
    '''
    DEBUG: print log messages or not
    return: artist, song, plain_lyric, dynamic_lyric
            and if DEBUG is specified, it will return the whole lyric additionally
            if dynamic_lyric is not supported, than the return dynamic_lyric will be a blank string

    Note: that the first two line of plain_lyric will be the song name & the aritst
    '''
    # google for lyric's urls
    urls = google_lyric(artist, song, DEBUG=DEBUG)

    for url in urls:
        if 'mojim' in url:
            print('getting data from: {}'.format(url))

            # download from url & parse tree
            tree = get_html_tree(url, DEBUG=DEBUG)

            if tree.xpath('//dl[@id="fsZx1"]'):
                if DEBUG == True:
                    artist, song, plain_lyric, dynamic_lyric, lyric = parse_artist_song_lyric(tree, DEBUG=True)
                else:
                    artist, song, plain_lyric, dynamic_lyric = parse_artist_song_lyric(tree)

                if DEBUG == True and not dynamic_lyric:
                    print('QQ: No dynamic lyric supported')

                if DEBUG == True:
                    return (artist, song, plain_lyric, dynamic_lyric, lyric)
                else:
                    return (artist, song, plain_lyric, dynamic_lyric)
