# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 19:06:54 2020

@author: AKASH DIXIT
"""

import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
subscription_key = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
headers = { 
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key
}
body={
    "personGroupId": "friends",
    "faceIds": [
        
        "c39af4f1-e0f2-4f3f-a505-6155423d2ea1"
        
    ]
    
}
params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('centralindia.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/identify?%s" % params, str(body), headers)
    response = conn.getresponse()
    data = response.read()
    #print(data)
    d= json.loads(data)
    #print(type(d))
    s= d[0]['candidates'][0]['personId']
    
    #print(s)
    if s == "7cc20792-2367-4ad2-b046-2073478bc5d7":
        print("AKASH")
    else:
        print("NOT FOUND")
#    my_json = data.decode('utf8').replace("'", '"')
#    #print(my_json)
#    r = json.loads(my_json)
#    s = json.dumps(r, indent=4, sort_keys=True)
#    print(type(s))
#    for a in s:
#        print(a["candidates"]["personId"])
    
    #print(r)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
