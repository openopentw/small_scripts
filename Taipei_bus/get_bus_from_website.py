"""
author: openopentw(YJC)
description:
usage:
"""

import urllib

from urllib import request

import lxml.html
import lxml.etree

import re
from pprint import pprint

def get_html_tree(url, DEBUG=False):
    """Download html code from url and parse tree.
    Args:
        url: The url where you want to downlaod and parse tree.
        DEBUG: To print log messages or not.
               [print (True) / not print (False)]
    Return:
        A lxml-tree which is parsed from the url given.
    """
    if DEBUG == True:
        print('getting data from: {}'.format(url))
    h = {'User-Agent':'Mozilla/5.0'}
    response = request.Request(url, headers=h)
    data = request.urlopen(response).read().decode('utf8')
    tree = lxml.html.fromstring( data )
    return tree

def get_bus_time(bus_name, IS_GO=True):
    """Get a tuple of bus time and the update time.
    Args:
        IS_GO: The direction of bus.
               [go(True) / back(False)]
    Returns:
        A tuple and a string which corresponds to the update-time.

        The tuple containing many tuples. Each tuple corresponds to a bus-stop, and it contains
        stop-name and coming-time. If there is a bus just coming, the tuple will include one more
        thing: the bus-name. Therefore, the formatted is:

        ( ('bus_stop', 'time', ('bus_id', {before / after})),
          ('bus_stop', 'time', ('bus_id', {before / after})), ... )

        , where before(False) / after(True). For example:

        (('捷運善導寺站', '4分'),
         ('成功中學(林森)', '4分', ('312-FR', False)), ... )

    Requires:
        function: get_html_tree()
    """

    tree = get_html_tree( 'http://pda.5284.com.tw/MQS/businfo2.jsp?routename=' + bus_name )
    nodes = tree.xpath('//table//tr[@class="tte{0}1" or @class="tte{0}2"]'.format('go' if IS_GO else 'back'))

    bus_times = ()
    for i,node in enumerate(nodes):

        stop_name = node.xpath('td//a')[0].text
        coming_time_and_bus = node.xpath('td[@align="center"]//text()')
        coming_bus = node.xpath('td[@align="center"]//font//text()')

        if coming_bus:
            # TODO: maybe the element of coming_bus will be more, not only one
            coming_bus_index = coming_time_and_bus.index(coming_bus[0])

            if coming_bus_index == 0:
                bus_time = (stop_name, coming_time_and_bus[1], (coming_time_and_bus[0], False))
            else:
                bus_time = (stop_name, coming_time_and_bus[0], (coming_time_and_bus[1], True))
        else:
            bus_time = (stop_name, coming_time_and_bus[0])

        bus_times += (bus_time,)

    update_time_data = tree.xpath('//span[@class="updatetime"]//text()')[0]
    update_time = re.findall('\d\d:\d\d:\d\d', update_time_data)[0]

    return (bus_times, update_time)

def search_time_bus_stop(bus_name, IS_GO, stop_name):
    """
    Args:
        stop_name:
                For example: '捷運公館站'
    Returns:
        a tuple bus time and
        For example: ('15分', '18:57:35')
    """

    bus_times, update_time = get_bus_time(bus_name, IS_GO)

    for bus_time in bus_times:
        if bus_time[0] == stop_name:
            return (bus_time[1], update_time)
