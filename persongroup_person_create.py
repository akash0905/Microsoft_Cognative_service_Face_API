# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 21:31:16 2019

@author: AKASH DIXIT
"""

import http.client, urllib.request, urllib.parse, urllib.error, base64

subscription_key = 'xxxxxxxxxxxxxxxxxxxxxxxxx'

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key':subscription_key
}

params = urllib.parse.urlencode({
        
        "personGroupId": "friends"
})

body = {
        "name": "akash", 
        "userData": "indus employee"
        }

try:
    conn = http.client.HTTPSConnection('centralindia.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/persongroups/friends/persons?%s" % params, str(body), headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))