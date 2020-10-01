# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 20:24:17 2019

@author: AKASH DIXIT
"""
import http.client, urllib.request, urllib.parse, urllib.error, base64
subscription_key = "xxxxxxxxxxxxxxxxxxxxxxxxx"

#faceListId = 0
headers = {
    # Request headers
    "Content-Type": "application/json",
    "Ocp-Apim-Subscription-Key": subscription_key
}

body = {
  "name": "face_list_1",
  "userData": "AKASH DIXIT face list",
  "recognitionModel": "recognition_02"
}

params = urllib.parse.urlencode({
#        "faceListId": "5"
})

try:
    conn = http.client.HTTPSConnection('centralindia.api.cognitive.microsoft.com')
    conn.request("PUT", "/face/v1.0/faceLists/2?%s" % params, str(body), headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    print(response)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))


