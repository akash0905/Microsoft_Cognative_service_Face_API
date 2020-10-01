# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 21:21:10 2019

@author: AKASH DIXIT
"""

import http.client, urllib.request, urllib.parse, urllib.error

subscription_key = 'xxxxxxxxxxxxxxxxxxxxxxxxx'

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key':subscription_key
}

params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('centralindia.api.cognitive.microsoft.com')
    conn.request("DELETE", "/face/v1.0/persongroups/mangal1?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))