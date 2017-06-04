# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 20:04:30 2017

@author: weiju
"""

import cv2
import numpy as np
cap=cv2.VideoCapture('2.mp4')
frame_number = int(cap.get(7))

for i in range(frame_number):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(5,5),1.5)  
    #hough transform
    circles1 = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,
    2000,param1=200,param2=30,minRadius=100,maxRadius=200)
    try:
        circles = circles1[0,:,:]#提取为二维
    except:
        circles=np.array([[0,0,0]])
    
    print(circles)
    for i in circles[:]: 
        cv2.circle(img,(i[0],i[1]),i[2],(255,0,0),5)#画圆
        cv2.circle(img,(i[0],i[1]),2,(255,0,255),10)#画圆心
    cv2.imshow('img',img)
    if cv2.waitKey(100) & 0xFF == ord('q'):#如果输入ESC退出
        break
cv2.destroyAllWindows()