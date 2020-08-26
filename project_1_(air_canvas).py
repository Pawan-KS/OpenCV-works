import cv2
import numpy as np
from stackimg import stackImages as stacker
def r(x):
    return cv2.resize(x,(500,500))

def preprocessing(img,th):
    img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower = np.array(th[:3])
    upper = np.array(th[3:])
    mask = cv2.inRange(img_hsv, lower, upper)
    mask = cv2.GaussianBlur(mask,(5,5),1)
    return mask

def getcontour(img):
    contours,hhy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=640,0,0,0
    for c in contours:
        area = cv2.contourArea(c)
        if area>10:
            cv2.drawContours(frame_temp,c,-1,(255,0,0),4)
            peri = cv2.arcLength(c,True)
            approx = cv2.approxPolyDP(c,0.02*peri,True)
            x,y,w,h = cv2.boundingRect(approx)
    return (x+w//2,y+h//4)

#video=[]
def drawon(img,coord_list,color,xb,yb):
    for coord in coord_list:
        cv2.circle(img,coord,8,color,cv2.FILLED)
    cv2.imshow('Air Canvas',img)
    #video.append(img)

cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)
cam.set(10,150)
th = [138,134,54,179,255,255]
# cam = cv2.VideoCapture('resources/canvas.mp4')
# th=[80,190,140,179,255,255]
coord_list=[]
clear=0
xb=120
yb=75
color = (0,0,255)
while True:
    ss, frame = cam.read()
    frame = cv2.flip(frame,1)
    # frame = cv2.rotate(frame,0)
    frame_temp = frame.copy()
    frame_res = frame.copy()
    cv2.rectangle(frame_res,(0,0),(xb,yb),(255,0,255),cv2.FILLED)
    cv2.rectangle(frame_res,(xb+40,0),(2*xb+40,yb),(255,0,0),cv2.FILLED)
    cv2.rectangle(frame_res, (2*xb+80,0),(3*xb+80,yb), (0,255,0), cv2.FILLED)
    cv2.rectangle(frame_res, (3*xb+120,0),(4*xb+120,yb), (0,0,255), cv2.FILLED)
    cv2.putText(frame_res,'CLEAR ALL         BLUE           GREEN           RED',(0,yb//2),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,0,0))
    mask = preprocessing(frame_temp,th)
    coord = getcontour(mask)
    if coord[0]<xb and coord[1]<yb:
        coord_list=[]
    elif coord[0]>xb+40 and coord[0]<2*xb+40 and coord[1]<yb:
        color = (255,0,0)
        coord_list = []
    elif coord[0]>2*xb+80 and coord[0]<3*xb+80 and coord[1]<yb:
        color = (0,255,0)
        coord_list = []
    elif coord[0]>3*xb+120 and coord[0]<4*xb+120 and coord[1]<yb:
        color = (0,0,255)
        coord_list = []
    coord_list.append(coord)
    drawon(frame_res,coord_list,color,xb,yb)
    # comb = stacker(1,[[frame,mask,frame_temp]])
    # cv2.imshow('processing_parts',comb)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

