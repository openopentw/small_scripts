'''
@author: openopentw(YJC)
@description:
@usage:
'''

import urllib
from urllib import request
import lxml.html
import lxml.etree

# download HTML CODE from url & PARSE TREE
def get_html_tree(url, DEBUG=False):# {{{
    '''
    @DEBUG: print log messages or not
    @return: a file tree which is parsed from url given
    '''
    if DEBUG == True:
        print('getting data from: {}'.format(url))
    h = {'User-Agent':'Mozilla/5.0'}
    response = request.Request(url, headers=h)
    data = request.urlopen(response).read().decode('utf8')
    tree = lxml.html.fromstring( data )
    return tree
# }}}

def get_bus_time(bus_name, IS_GO=True):
    '''
    @IS_GO: The direction of bus. go(True), back(False)
    @return: 2 lists of tuples which is formatted as: ('bus_stop', 'time', ('bus_id', {0 or 1}))
                                                                               , where 0(before), 1(after)
            e.g.
            [ ('捷運善導寺站', '4分'),
              ('成功中學(林森)', '4分', ('312-FR', 0)) ]
    '''

    tree = get_html_tree( 'http://pda.5284.com.tw/MQS/businfo2.jsp?routename=' + bus_name )
    nodes = tree.xpath('//table//tr[@class="tte{0}1" or @class="tte{0}2"]'.format('go' if IS_GO else 'back'))
    bus_time_list = []
    for node in nodes:

        all_time = node.xpath('td[@align="center"]//text()')
        font = node.xpath('td[@align="center"]//font//text()')
        if font:
            html = str(lxml.etree.tostring( nodes[-11].xpath('td[@align="center"]')[0], encoding='unicode'))
            pos = html.index(font[0])


        bus_time = ( node.xpath('td//a')[0].text ,
                    node.xpath('td[@align="center"]//text()') )


        bus_time_list += [bus_time]


    updatetime_data = tree.xpath('//span[@class="updatetime"]//text()')[0]
    updatetime = re.findall('\d\d:\d\d:\d\d', updatetime_data)

    return (bus_dicts, updatetime)

def search_time_bus_stop(bus_name, stop_name):
    return
