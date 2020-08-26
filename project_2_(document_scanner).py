import cv2
import numpy as np
from stackimg import stackImages as stacker
def r(x):
    return cv2.resize(x,(480,640))

def preprocessing(img):
    ker = np.ones((5,5))
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = cv2.Canny(img,200,200)
    img = cv2.dilate(img,ker,iterations=2)
    img = cv2.erode(img,ker,iterations=1)
    return img

def getcontours(img):
    contours, hhy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    max_ar = 0
    biggest = np.array([])
    for c in contours:
        area = cv2.contourArea(c)
        if area>5000:
            cv2.drawContours(imgc, c, -1, (255, 0, 0), 10)
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            side = len(approx)
            if side==4:
                if area>=max_ar:
                    biggest = approx
                    max_ar = area
    return biggest

def reorder(coords):
    new_coords = np.zeros((4,1,2),np.int32)
    coords = coords.reshape((4,2))
    add = coords.sum(1)
    new_coords[0] = coords[np.argmin(add)]
    new_coords[3] = coords[np.argmax(add)]
    diff = np.diff(coords,axis=1)
    new_coords[1] = coords[np.argmin(diff)]
    new_coords[2] = coords[np.argmax(diff)]
    return new_coords

def getwarp(img,coords):
    coords = reorder(coords)
    pt1 = np.float32(coords)
    pt2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    matrix = cv2.getPerspectiveTransform(pt1, pt2)
    return cv2.warpPerspective(img, matrix, (width, height))


#img = cv2.imread('resources/paper.jpg')
cam = cv2.VideoCapture('resources/docvid2.mp4')
# cam.set(3,640)
# cam.set(4,480)
# cam.set(10,150)
width, height = 480, 640
while True:
    ss, img = cam.read()
    #img = cv2.flip(img, 1)
    img = cv2.rotate(img,0)
    imgc = img.copy()
    proc_img = preprocessing(img)
    coords = getcontours(proc_img)
    if coords.size!=0:
        warp_img = getwarp(img,coords)
        res_img = warp_img[20:warp_img.shape[0]-20,20:warp_img.shape[1]-20]
        res_img = cv2.resize(res_img,(width,height))
        comb = stacker(0.7,[[r(img),r(imgc)],[r(warp_img),res_img]])
        cv2.imshow('all',comb)
    else:
        comb = stacker(0.7, [[r(img), r(imgc)], [r(img), r(img)]])
        cv2.imshow('all', comb)
    #cv2.imshow('res',res_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break