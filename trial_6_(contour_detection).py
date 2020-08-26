import cv2
import numpy as np
from stackimg import stackImages as stacker
def r(x):
    return cv2.resize(x,(500,500))
def empty(x):
    pass
img = cv2.imread('resources/shapes.png')
imgc = img.copy()
imgb = np.zeros_like(img)

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray,(5,5),1)
img_canny = cv2.Canny(img_blur,10,50)

def getcontour(x):
    contours,hhy = cv2.findContours(x,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for i,c in enumerate(contours):
        area = cv2.contourArea(c)
        print('area '+str(i)+'--> ',area)
        if area>500:
            cv2.drawContours(imgc,c,-1,(255,0,0),4)
            peri = cv2.arcLength(c,True)
            print('perimeter '+str(i)+'--> ',peri)
            approx = cv2.approxPolyDP(c,0.02*peri,True)
            sides = len(approx)
            print('detected sides in '+str(i)+'--> ',sides)
            x,y,w,h = cv2.boundingRect(approx)
            cv2.rectangle(imgc,(x,y),(x+w,y+h),(0,0,255),4)
            if sides==3: type='tri'
            elif sides==4:
                ar=w/h
                if ar>=0.95 and ar<=1.05: type='square'
                else: type='rectangle'
            elif sides==8: type='circle'
            else: type='polygon_'+str(sides)
            cv2.putText(imgc,type,(x+(w//2)-50,y+(h//2)),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),2)

getcontour(img_canny)
comb = stacker(0.6,[[img,img_gray,img_blur],[img_canny,imgc,imgb]])
cv2.imshow('--',comb)

cv2.waitKey(0)