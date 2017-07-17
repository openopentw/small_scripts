'''
author: openopentw(YJC)
description:
usage:
'''

import get_bus_from_website as get_bus
import json

queries = (('208', 'go', '捷運公館站'),
           ('208%E7%9B%B4', 'go', '捷運公館站'),   # 208直
           ('671', 'go', '捷運公館站'),
           ('208', 'back', '開南商工'))

for query in queries:
    is_go = True if query[1] == 'go' else False
    ret = get_bus.search_time_bus_stop(query[0], is_go, query[2])
    break

# print('yjc is so handsome.')
# print( json.dumps([123, 12]) )
print( json.dumps(ret) )
