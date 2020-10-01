# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 16:53:02 2019

@author: AKASH DIXIT
"""

import http.client, urllib.request, urllib.parse, urllib.error, base64
subscription_key = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': subscription_key
}

params = urllib.parse.urlencode({
    "personGroupId" : "friends",
    'returnRecognitionModel': 'false',
})

try:
    conn = http.client.HTTPSConnection('centralindia.api.cognitive.microsoft.com')
    conn.request("GET", "/face/v1.0/persongroups/friends?returnRecognitionModel=false?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
