import cv2
import numpy as np
from stackimg import stackImages as stacker
def r(x):
    return cv2.resize(x,(500,500))

FC = cv2.CascadeClassifier('resources/haarcascade_frontalface_default.xml')
img = r(cv2.imread('resources/profilepic.jpg'))
imgc = img.copy()
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = FC.detectMultiScale(img_gray,1.1,4)
for (x,y,w,h) in faces:
    cv2.rectangle(imgc,(x,y),(x+w,y+h),(0,0,255),2)

comb = stacker(1,[[img,imgc]])
cv2.imshow('--',comb)
cv2.waitKey(0)
