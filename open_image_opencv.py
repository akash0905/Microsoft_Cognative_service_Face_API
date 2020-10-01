# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 22:54:42 2019

@author: AKASH DIXIT
"""
import numpy as np
import cv2
import time


image_path = cv2.imread("C:/Users/AKASH DIXIT/Desktop/shefali.jpg")

cv2.imshow("face", image_path)
        
time.sleep(5)
cv2.destroyAllWindows()
#

#
# importing cv2  
#import cv2  
#  
## path  
#path = r'C:\Users\AKASH DIXIT\Desktop\bill.jpeg'
#  
## Reading an image in default mode 
#image = cv2.imread(path) 
#  
## Window name in which image is displayed 
##window_name = 'image'
#  
## Using cv2.imshow() method  
## Displaying the image  
#cv2.imshow('image', image)  