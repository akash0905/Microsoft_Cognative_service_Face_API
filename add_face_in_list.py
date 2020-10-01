# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 22:43:14 2019

@author: AKASH DIXIT
"""
for i in range(1, 200):
    import http.client, urllib.request, urllib.parse, urllib.error
    import time
    subscription_key = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
    
    
    image_path = "C:/Users/AKASH DIXIT/Documents/GitHub/Microsoft_Cognitive_Services_Face_API/dataSet/user.2."+str(i)+".jpg"
    with open(image_path, 'rb') as f:
        img_data = f.read()    # type: object
    
    
    
    headers = {
        # Request headers
        "Content-Type": "application/octet-stream",
        "Ocp-Apim-Subscription-Key": subscription_key
    }
    
    params = urllib.parse.urlencode({
        # Request parameters
        'faceListId': '2'
    
    })
    
    try:
        conn = http.client.HTTPSConnection('centralindia.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/faceLists/2/persistedFaces?%s" % params, img_data, headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
    
    time.sleep(4)