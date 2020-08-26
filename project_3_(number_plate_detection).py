import cv2
import numpy as np
from stackimg import stackImages as stacker
def r(x):
    return cv2.resize(x,(400,100))

cam = cv2.VideoCapture('resources/numplates.mp4')
# cam.set(3,640)
# cam.set(4,480)
# cam.set(10,150)
NPC = cv2.CascadeClassifier('resources/haarcascade_russian_plate_number.xml')
count=0
while True:
    ss, img = cam.read()
    imgc = img.copy()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plates = NPC.detectMultiScale(img_gray, 1.1, 4)
    for (x, y, w, h) in plates:
        area = w*h
        if area > 500 and area<8000:
            cv2.rectangle(imgc, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(imgc,'Number Plate',(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.5,(0,0,255),1)
    cv2.imshow('--', imgc)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        crop_img = img[y:y + h, x:x + w]
        cv2.imwrite('resources/num_plates/numplate_'+str(count)+'.jpg',r(crop_img))
        cv2.rectangle(imgc,(0,100),(img.shape[1],300),(0,255,0),cv2.FILLED)
        cv2.putText(imgc,'SAVED',(200,200),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,0),2)
        cv2.imshow('--',imgc)
        cv2.waitKey(300)
        count+=1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break