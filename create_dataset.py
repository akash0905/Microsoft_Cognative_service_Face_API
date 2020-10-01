# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 19:25:30 2019

@author: AKASH DIXIT
"""

# -*- coding: utf-8 -*-


import cv2
import numpy as np

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam=cv2.VideoCapture(0);
id= input('enter user id: ')
sampleNum=0;
while(True):
    ret,img=cam.read();
    faces = faceDetect.detectMultiScale(img, 1.3, 5);
#for(x,y,w,h) in faces:
    sampleNum=sampleNum+1;
    cv2.imwrite("dataSet/user."+str(id)+"."+str(sampleNum)+".jpg",img)
    #cv2.rectangle(img)
    cv2.waitKey(100);
    cv2.imshow("Face",img);
    
    
    
    
    cv2.waitKey(1);
    if(sampleNum>200):
        break
cam.release()
cv2.destroyAllWindows()
                           
