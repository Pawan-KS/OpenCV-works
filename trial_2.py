import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
print(img.shape)

cv2.line(img, (0,0),(img.shape[1],img.shape[0]),(255,0,0))
cv2.rectangle(img, (100,200),(300,400),(0,0,255),cv2.FILLED)
cv2.circle(img,(400,100),100,(200,100,200),5)
cv2.putText(img,'FIRST PROJECT',(200,490),cv2.FONT_HERSHEY_COMPLEX,1,(0,200,0))

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow('image', img)
cv2.waitKey(0)