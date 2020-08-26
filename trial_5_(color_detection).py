import cv2
import numpy as np
from stackimg import stackImages as stacker
def r(x):
    return cv2.resize(x,(500,500))
def empty(x):
    pass
img = r(cv2.imread('resources/profilepic.jpg'))


cv2.namedWindow('trackbars')
cv2.resizeWindow('trackbars',(640,300))
cv2.createTrackbar('hue min','trackbars',80,179,empty)
cv2.createTrackbar('hue max','trackbars',179,179,empty)
cv2.createTrackbar('sat min','trackbars',190,255,empty)
cv2.createTrackbar('sat max','trackbars',255,255,empty)
cv2.createTrackbar('val min','trackbars',140,255,empty)
cv2.createTrackbar('val max','trackbars',255,255,empty)

# while True:
#     img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#     h_min = cv2.getTrackbarPos('hue min','trackbars')
#     h_max = cv2.getTrackbarPos('hue max','trackbars')
#     s_min = cv2.getTrackbarPos('sat min','trackbars')
#     s_max = cv2.getTrackbarPos('sat max','trackbars')
#     v_min = cv2.getTrackbarPos('val min','trackbars')
#     v_max = cv2.getTrackbarPos('val max','trackbars')
#     lower = np.array([h_min,s_min,v_min])
#     upper = np.array([h_max, s_max, v_max])
#     mask = cv2.inRange(img_hsv,lower,upper)
#     img_res = cv2.bitwise_and(img, img, mask=mask)
#     img_res1 = cv2.bitwise_or(img, img, mask=mask)
#     img_res2 = cv2.bitwise_xor(img, img, mask=mask)
#
#     comb = stacker(0.7,[[img,img_hsv,mask],[img_res,img_res1,img_res2]])
#     cv2.imshow('images',comb)
#
#     cv2.waitKey(1)

cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)
cam.set(10,100)
while True:
    ss, img = cam.read()
    img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos('hue min','trackbars')
    h_max = cv2.getTrackbarPos('hue max','trackbars')
    s_min = cv2.getTrackbarPos('sat min','trackbars')
    s_max = cv2.getTrackbarPos('sat max','trackbars')
    v_min = cv2.getTrackbarPos('val min','trackbars')
    v_max = cv2.getTrackbarPos('val max','trackbars')
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(img_hsv,lower,upper)
    img_res = cv2.bitwise_and(img, img, mask=mask)
    img_res1 = cv2.bitwise_and(cv2.cvtColor(img,cv2.COLOR_BGR2RGB), img, mask=mask)
    img_res2 = cv2.bitwise_and(img, cv2.cvtColor(img,cv2.COLOR_BGR2RGB), mask=mask)

    comb = stacker(0.5,[[img,img_hsv,mask],[img_res,img_res1,img_res2]])
    cv2.imshow('images',comb)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# cap = cv2.VideoCapture('resources/canvas.mp4')
# while True:
#     ss, img = cap.read()
#     img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#     h_min = cv2.getTrackbarPos('hue min','trackbars')
#     h_max = cv2.getTrackbarPos('hue max','trackbars')
#     s_min = cv2.getTrackbarPos('sat min','trackbars')
#     s_max = cv2.getTrackbarPos('sat max','trackbars')
#     v_min = cv2.getTrackbarPos('val min','trackbars')
#     v_max = cv2.getTrackbarPos('val max','trackbars')
#     lower = np.array([h_min,s_min,v_min])
#     upper = np.array([h_max, s_max, v_max])
#     mask = cv2.inRange(img_hsv,lower,upper)
#     # img_res = cv2.bitwise_and(img, img, mask=mask)
#     # img_res1 = cv2.bitwise_and(cv2.cvtColor(img,cv2.COLOR_BGR2RGB), img, mask=mask)
#     # img_res2 = cv2.bitwise_and(img, cv2.cvtColor(img,cv2.COLOR_BGR2RGB), mask=mask)
#
#     comb = stacker(0.5,[[img,img_hsv,mask]])
#     cv2.imshow('images',comb)
#
#     if cv2.waitKey(50) & 0xFF == ord('q'):
#         break