# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 17:21:47 2017

@author: weiju
"""

import cv2
cap=cv2.VideoCapture('2.mp4')
frame_number = int(cap.get(7))
frame_FPS = int(cap.get(5))
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),   
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))  
print(frame_number,frame_FPS,size)
cap.set(cv2.CAP_PROP_POS_FRAMES, 55)
ret, frame = cap.read()
cv2.imshow('img',frame)
if cv2.waitKey(0)==27:#如果输入ESC退出
    cv2.destroyAllWindows()

#for i in range(frame_number):
#    ret, frame = cap.read()
#    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#    cv2.imshow('img',gray)
# 
#    if cv2.waitKey(10) & 0xFF == ord('q'):#如果输入ESC退出
#        break
#cv2.destroyAllWindows()
cap.release()
