# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 18:23:05 2017

@author: weiju
"""

import cv2
import numpy as np

img = cv2.imread('1.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#灰度图像 

#hough transform
circles1 = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,
2000,param1=200,param2=30,minRadius=50,maxRadius=100)
try:
    circles = circles1[0,:,:]#提取为二维
except:
    circles=np.array([[0,0,0]])
circles = np.uint16(np.around(circles))#四舍五入，取整
print(circles)
for i in circles[:]: 
    cv2.circle(img,(i[0],i[1]),i[2],(255,0,0),5)#画圆
    cv2.circle(img,(i[0],i[1]),2,(255,0,255),10)#画圆心
cv2.imshow('gray',gray)
cv2.imshow('img',img)
if cv2.waitKey(0)==27:#如果输入ESC退出
    cv2.destroyAllWindows()
