# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 22:31:46 2019

@author: AKASH DIXIT
"""

import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'xxxxxxxxxxxxxxxxxxxxxxxxx',
}

params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('centralindia.api.cognitive.microsoft.com')
    conn.request("DELETE", "/face/v1.0/faceLists/3?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))