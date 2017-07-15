"""
author: openopentw(YJC)
description:
usage:
"""

import lxml.html
import lxml.etree
import re
import urllib
import pandas as pd

from urllib import request
# from pprint import pprint

def preprocess_string(data):
    return re.sub(' \(.*\)', '', data)

def get_html_tree(url, func_preprocess, DEBUG=False):
    """Download html code from url, preprocess on the string and parse tree.
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

    data = func_preprocess(data)

    tree = lxml.html.fromstring( data )
    return tree

# get tree & dataframe
url = "https://monitor.csie.ntu.edu.tw/status.html"
tree = get_html_tree(url, preprocess_string)
usage = pd.read_html( lxml.html.tostring(tree) )[0]

# change column header
new_header = usage.iloc[0]
usage = usage[1:].rename(columns=new_header)

# change row header
usage.index = usage['Host'].values
usage.drop('Host', 1, inplace=True)

# create a usage dataframe
usage_score = usage.copy(deep=True)

# calculate basic score of each host
score = {'normal': 0, 'low': 1, 'medium': 3, 'high': 5}
for node in tree.xpath('//table//tr')[1:]:
    host = node.xpath('td')[0].text
    for i,td in enumerate(node.xpath('td')[1:]):
        usage_score.loc[host][i] = score[ td.attrib['class'] ]
usage['Score'] = usage_score.sum(axis=1)

# split the 3 oasises to another dataframe  # will not use it
no_intensive_job = usage.iloc[-3:]
usage = usage.iloc[:-3]

# sort by score and number of user
usage = usage.sort_values(['Score', 'Users'], ascending=[True, True])

# print the less score and less user
print(usage.index[0])
