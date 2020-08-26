import cv2
import numpy as np
def r(x):
    return cv2.resize(x,(500,500))
img = r(cv2.imread('resources/cards.jpg'))
width,height = 250,350
pt1 = np.float32([[330,40],[500,130],[150,320],[360,460]])
pt2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pt1,pt2)
imgout = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow('original image',img)
cv2.imshow('one card',imgout)
cv2.waitKey(0)