# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 22:34:47 2019

@author: AKASH DIXIT
"""

import http.client, urllib.request, urllib.parse, urllib.error, base64

subscription_key = 'xxxxxxxxxxxxxxxxxxxxxxxxx'

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key':subscription_key
}

params = urllib.parse.urlencode({
        "personGroupId" : "friends"
})

try:
    conn = http.client.HTTPSConnection('centralindia.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/persongroups/friends/train?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))