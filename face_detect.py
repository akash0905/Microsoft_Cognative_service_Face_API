# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 20:34:21 2020

@author: SHEFALI MANGAL
"""

import http.client, urllib.request, urllib.parse, urllib.error
import os
import cv2
import requests
cam=cv2.VideoCapture(0)

subscription_key = '3c01f77e6d1744148871d96fad2ad42b'
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
    #conn.close()
#except Exception as e:
    #print("[Errno {0}] {1}".format(e.errno, e.strerror))

os.remove("C:/Users/AKASH DIXIT/Documents/GitHub/Microsoft_Cognitive_Services_Face_API/capturePerson/image.jpg")
cam.release()
cv2.destroyAllWindows()

