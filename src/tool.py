# -*- coding: utf-8 -*-
'''
Created on 2017. 4. 19.
@author: HyechurnJang
'''

import json
import time

def pretty(data):
    try: print(json.dumps(data, indent=2))
    except Exception as e:
        print(str(e))

def toFile(data):
    try:
        file_name = 'result-%d.txt' % int(time.time())
        print('toFile : %s' % file_name)
        with open(file_name, 'w') as fd:
            fd.write(json.dumps(data, indent=2))
        print('ok')
    except Exception as e:
        print(str(e))

def find(data_of_list, key, val):
    if isinstance(data_of_list, list):
        for data in data_of_list:
            if key in data and data[key] == val:
                return data
        else:
            print('"%s == %s" is not in list' % val)
            return None
    else:
        print('Input is not list')
        return None
