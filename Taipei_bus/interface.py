'''
@author: openopentw(YJC)
@description:
@usage:
'''

import get_bus_from_website as get_bus
import json

#          ['208',        '208直', '671']
bus_list = ['208', '208%E7%9B%B4', '671']
stop_list = ['捷運公館站', '開南商工']

ret_go = [1, 1, 1]
ret_back = [1, 0, 0]

go_lists = []
back_lists = []
for i, bus in enumerate(bus_list):
    # go_dict, back_dict = get_bus.get_bus_dict(bus, ret_go[i], ret_back[i])
    go_list, back_list = get_bus.get_bus_list(bus, ret_go[i], ret_back[i])
    if go_list:
        go_lists += [go_list]
    if back_list:
        back_lists += [back_list]

print( json.dumps([go_lists, back_lists]) )
