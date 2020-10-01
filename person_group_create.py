# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 16:37:07 2019

@author: AKASH DIXIT
"""

import http.client, urllib.request, urllib.parse, urllib.error


subscription_key = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
headers = {
    # Request headers
    'Content-Type': 'application/json',
    "Ocp-Apim-Subscription-Key": subscription_key
}

params = urllib.parse.urlencode({
        "personGroupId" : "friends"
            })
body= {
       "name": "itm"
     
     }

try:
    conn = http.client.HTTPSConnection('centralindia.api.cognitive.microsoft.com')
    conn.request("PUT", "/face/v1.0/persongroups/friends?%s" % params, str(body), headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
