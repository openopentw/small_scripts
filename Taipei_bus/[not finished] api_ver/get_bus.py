'''
@author: openopentw(YJC)
@description:
@usage:
'''

import urllib
from urllib import request
import gzip
import json


bus_list = ['208', '208直', '671']


ROUTE_url = 'http://data.taipei/bus/ROUTE'
EstimateTime_url = 'http://data.taipei/bus/EstimateTime'

def get_dict_data(url):
    tmp_json_gz = request.urlretrieve(url)
    with gzip.open(tmp_json_gz[0], 'rb') as f:
        dict_data = json.loads(f.read().decode('utf-8'))
    return dict_data

ROUTE = get_dict_data(ROUTE_url)
EstimateTime = get_dict_data(EstimateTime_url)

pathName = [ path['pathAttributeName'] for path in ROUTE['BusInfo'] ]
bus_name_id = { bus_name : ROUTE['BusInfo'][pathName.index( bus_name )]['Id']
                    for bus_name in bus_list }
