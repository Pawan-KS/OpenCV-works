import cv2
import numpy as np
from stackimg import stackImages as stacker
kernel = np.ones((5,5),np.uint8)

def r(x):
    return cv2.resize(x,(512,512))

# img = r(cv2.imread('resources/profilepic.jpg'))
# def hflip(y):
#     x=y.copy()
#     for i in range(x.shape[1]//2):
#         temp=x[:,i,:].copy()
#         x[:,i,:]=x[:,x.shape[1]-i-1,:]
#         x[:, x.shape[1]-i-1, :]=temp
#     return x
# cv2.imshow('flip img',hflip(img))
# cv2.imshow('pic',img)
# cv2.waitKey(0)

# cap = cv2.VideoCapture('resources/video.mp4')
# while True:
#     ss, frame = cap.read()
#     frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     frame2 = cv2.Canny(frame,50,70)
#     comb = stacker(1,[[r(frame),r(frame1),r(frame2)]])
#     cv2.imshow('video',comb)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break

# FC = cv2.CascadeClassifier('resources/haarcascade_frontalface_default.xml')
#
# cam = cv2.VideoCapture(0)
# cam.set(3,640)
# cam.set(4,480)
# cam.set(10,100)
# while True:
#     ss, frame = cam.read()
#     frame1 = cv2.Canny(frame, 50,70)
#     frame2 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     frame3 = frame.copy()
#     faces = FC.detectMultiScale(frame2,1.1,4)
#     for (x,y,w,h) in faces:
#         cv2.rectangle(frame3,(x,y),(x+w,y+h),(0,0,255),2)
#     # frame2 = cv2.dilate(frame, kernel, iterations=2)
#     # frame3 = cv2.erode(frame,kernel,iterations=2)
#     comb = stacker(1,[[r(frame),r(frame1)],[r(frame2),r(frame3)]])
#     cv2.imshow('video',comb)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break

# img = cv2.imread('resources/profilepic.jpg')
#
# img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# img_rev = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# img_blur = cv2.GaussianBlur(img,(21,21),0)
# img_canny = cv2.Canny(img,50,70)
# img_dil = cv2.dilate(img_canny,kernel,iterations=2)
# img_ero = cv2.erode(img_dil,kernel,iterations=2)
#
# cv2.imshow('gray img',img_gray)
# cv2.imshow('rev img',img_rev)
# cv2.imshow('blur img',img_blur)
# cv2.imshow('canny img',img_canny)
# cv2.imshow('dilated img',img_dil)
# cv2.imshow('eroded img',img_ero)
# cv2.waitKey(0)

# img = cv2.imread('resources/profilepic.jpg')
# print(img.shape)
# img_resize = cv2.resize(img,(300,100))
# print(img_resize.shape)
# img_crop = img[1000:1500,1000:1300]
# print(img_resize.shape)
# #cv2.imshow('resize img', img_resize)
# cv2.imshow('crop pic',img_crop)
# cv2.waitKey(0)
