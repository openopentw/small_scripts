'''
author: openopentw(YJC)
description: download & parse the lyrics on the mojim webpage
output: 2 files
    - {plain_lyric}.txt
    - {dynamic_lyric}.lrc
usage:
    for e.g.
    $> python interface.py 七里香
    $> python interface.py 七里香 -a 周杰倫
    $> python interface.py 七里香 -o lyric_folder
    $> python interface.py 七里香 -n (歌詞)周杰倫-七里香
'''

import os
import sys
import argparse
import download_mojim

# parse args
parser = argparse.ArgumentParser()
parser.add_argument('song', help='the SONG you want to get lyric with')
parser.add_argument('-a', default='', help='the ARTIST who sing the song')
parser.add_argument('-o', default='./lyric', help='the output DIRECTORY')
parser.add_argument('-n', help='the output FILENAME, if not define, will use "{artise} - {song name}"')
args = parser.parse_args(sys.argv[1:])

# get artist & song & output_dir
artist = args.song
song = args.a
output_dir = args.o

# make folder if it is not exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


# get lyric
artist, song, plain_lyric, dynamic_lyric = download_mojim.main_get_lyric(artist, song)


# specify output file name
print('find the song: {}, sung by {}.'.format(song, artist))
if args.n:
    plain_path = os.path.join(output_dir, '{}.txt'.format(args.n))
    dynamic_path = os.path.join(output_dir, '{}.lrc'.format(args.n))
else:
    plain_path = os.path.join(output_dir, '{} - {}.txt'.format(artist, song))
    dynamic_path = os.path.join(output_dir, '{} - {}.lrc'.format(artist, song))

# output to file
print('saving plain lyric to: {}'.format(plain_path))
f = open(plain_path, 'w', encoding='utf8')
print(plain_lyric, file=f)
f.close()

if dynamic_lyric:
    print('saving dynamic lyrics to: {}'.format(dynamic_path))
    f = open(dynamic_path, 'w', encoding='utf8')
    print(dynamic_lyric, file=f)
    f.close()
else:
    print('QQ: No dynamic lyric support')
