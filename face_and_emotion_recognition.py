# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 20:34:21 2020

@author: AKASH DIXIT
"""

import http.client, urllib.request, urllib.parse, urllib.error
import os
import cv2
import requests
import json
import time
for i in range(0, 2):
    cam=cv2.VideoCapture(0)
    
    subscription_key = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
    ret,img=cam.read()
    cv2.imwrite("capturePerson/image"+".jpg",img)
    cv2.waitKey(100)
    cv2.imshow("Face",img)
    image_path = "C:/Users/AKASH DIXIT/Documents/GitHub/Microsoft_Cognitive_Services_Face_API/capturePerson/image.jpg"
    image_data = open(image_path, "rb").read()
    
    headers = {
        # Request headers
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': subscription_key,
    }
    
    params = urllib.parse.urlencode({
        # Request parameters
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'Age,emotion',
        
        'recognitionModel': 'recognition_01',
        'returnRecognitionModel': 'false',
        'detectionModel': 'detection_01',
    })
    
    #try:
        #conn = http.client.HTTPSConnection('centralindia.api.cognitive.microsoft.com')
        #conn.request("POST", "/face/v1.0/detect?%s" % params, headers=headers, data=image_data)
    face_recognition_url = "https://centralindia.api.cognitive.microsoft.com/face/v1.0/detect?%s" % params
    response = requests.post(face_recognition_url, headers=headers, data=image_data, params=params)
        #response = conn.getresponse()
    p = response.json()
    print(p)
    d = p[0]['faceId']
    for a in p:
        emo = a['faceAttributes']['emotion']
        value_max = max(emo.keys(), key=(lambda v: emo[v]))
        key_max = max(emo.keys(), key=lambda k: emo[k])
#        print(value_max)

        print('Maximum Value: ',emo[value_max])
        print('Maximum key: ',key_max)
    #print(d)
    
    headers1 = { 
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': subscription_key
    }
    body1={
        "personGroupId": "friends",
        "faceIds": [      
            d]
        
    }
    params1 = urllib.parse.urlencode({
    })
    
    try:
        conn = http.client.HTTPSConnection('centralindia.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/identify?%s" % params1, str(body1), headers1)
        response = conn.getresponse()
        data = response.read()
        #print(data)
        d= json.loads(data)
        #print(type(d))
        s= d[0]['candidates'][0]['personId']
        
        #print(s)
        if s == "7cc20792-2367-4ad2-b046-2073478bc5d7":
            print("shefali")
        else:
            print("NOT FOUND")
    
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
    
    os.remove("C:/Users/AKASH DIXIT/Documents/GitHub/Microsoft_Cognitive_Services_Face_API/capturePerson/image.jpg")
    i=i+1
    time.sleep(4)
cam.release()
cv2.destroyAllWindows()
#if p == "7cc20792-2367-4ad2-b046-2073478bc5d7"