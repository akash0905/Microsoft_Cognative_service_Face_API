# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 21:53:41 2019

@author: AKASH DIXIT
"""
for i in range(1, 200):
    import http.client, urllib.request, urllib.parse, urllib.error, base64
    import time
    subscription_key = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
    
    image_path = "C:/Users/AKASH DIXIT/Documents/GitHub/Microsoft_Cognitive_Services_Face_API/dataSet/user.2."+str(i)+".jpg"
    with open(image_path, 'rb') as f:
        img_data = f.read()  
    
    headers = {
        # Request headers
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key':subscription_key
    }
    
    params = urllib.parse.urlencode({
         "personGroupId": "friends",
         "personId": "09fc1671-a4cb-46ae-b604-4e942f04e56e",
        
        "userData": "akashs images",
        
        'detectionModel': 'detection_01',
    })
    
    
    
    
    try:
        conn = http.client.HTTPSConnection('centralindia.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/persongroups/friends/persons/09fc1671-a4cb-46ae-b604-4e942f04e56e/persistedFaces?%s" % params, img_data, headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
    
    time.sleep(4)