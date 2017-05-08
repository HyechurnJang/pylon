# -*- coding: utf-8 -*-
'''
Created on 2017. 4. 19.
@author: HyechurnJang
'''

import requests
requests.packages.urllib3.disable_warnings()

__session = requests.Session()

__serv_url = 'https://198.18.133.136'
__base_url = __serv_url + '/smc'
__rest_url = __base_url + '/rest'
headers = {'accept' : 'application/json'}

resp = __session.post(__base_url + '/j_spring_security_check',
                      headers={'Content-Type': 'application/x-www-form-urlencoded',
                               'Referer': __serv_url + '/lc-landing-page/',
                               'Origin': __serv_url},
                      data='j_username=admin&j_password=C1sco12345&submit=',
                      allow_redirects=True,
                      verify=False)

def get(url):
    print('Stealthwatch Get : %s' % url)
    try:
        resp = __session.get(__rest_url + url)
        if resp.status_code == 200:
            print('Stealthwatch Response Code : 200 OK\n')
            try: return resp.json()
            except: return resp.text
        elif resp.status_code == 400:
            print('Stealthwatch Response Code : 400 Bad Request\nGeneral error when fulfilling the request that would cause an invalid state, for example, domain validation errors or missing data\n')
        elif resp.status_code == 401:
            print('Stealthwatch Response Code : 401 Unauthorized\nError code response for missing or invalid authentication token. It indicates that the request can be retried once a valid authentication token has been acquired\n')
        elif resp.status_code == 404:
            print('Stealthwatch Response Code : 404 Not Found\nUsed when the requested resource is not found, whether because it does not exist, or for security reasons, the service wants to mask its existence\n')
        elif resp.status_code == 405:
            print('Stealthwatch Response Code : 405 Method Not Allowed\nA request was made of a resource using a request method not supported by that resource, for example, using GET on a write-only resource or using PUT on a read-only resource\n')
        elif resp.status_code == 500:
            print('Stealthwatch Response Code : 500 Internal Server Error\nThe general catch-all error when the server-side has an exception. In the event of a failure, the response body will contain a JSON response that should contain more information about what caused the operation to fail\n')
        else:
            print('Stealthwatch Response Code : %d\nUnknown\n' % resp.status_code)
        return None
    except Exception as e:
        print('Stealthwatch Error\n%s\n' % str(e))
        return None
