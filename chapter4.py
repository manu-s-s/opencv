import cv2
import numpy as np
img=np.zeros((512,512,3))
cv2.line(img,(0,0),(250,250),(0,255,255),5,)
cv2.rectangle(img,(10,10),(300,150),(0,255,0),cv2.FILLED)
cv2.putText(img,'opencv',(250,300),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,100),)
cv2.imshow('output',img)
cv2.waitKey()