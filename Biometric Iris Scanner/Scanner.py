import cv2
import numpy as np

img = np.zeros((500,500,3),dtype=np.unit8)
for r in range(50,200,20)
    cv2.circle(img,(250,250),r,(255,255,0),2)

for a in range(0,360,15):
    x = int(250 + 180*np.cos(np.radians(a)))
    y = int(250 + 180*np.sin(np.radians(a)))
    cv2.line(img,(250,250),(x,y),(0,255,255),1)

cv2.putText(img, "IRIS SCAN" , (170,450),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,(0,255,0),2)

cv2.imshow(" Iris Scanner", img)
cv2.waitkey(0)
    
