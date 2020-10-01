# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 23:33:16 2020

@author: AKASH DIXIT
"""

import http.client, urllib.request, urllib.parse, urllib.error, base64
subscription_key = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key':subscription_key
}

body = {
    "faceId1": "37a6b4dc-bb24-4d68-90f4-0dd3067498f9",
    "faceId2": "899ece3e-082d-475a-bc3a-35cf270605d7",
    
    }

params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('centralindia.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/verify?%s" % params, str(body), headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))