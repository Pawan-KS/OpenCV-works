import cv2
import numpy as np
from stackimg import stackImages as stacker

def r(x):
    return cv2.resize(x,(500,500))

img = r(cv2.imread('resources/profilepic.jpg'))

img_ver = stacker(0.75,[[img,img],[img,img],[img,img]])

cv2.imshow('ver',img_ver)
cv2.waitKey(0)