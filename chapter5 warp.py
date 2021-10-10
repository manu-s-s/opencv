import cv2
import numpy as np
width, height =250,350
img=cv2.imread('resources\images.jpeg')
point1=np.float32([[125,172],[210,135],[154,22],[73,55]])
point2=np.float32([[0,height],[width,height],[width,0],[0,0]])
matrix=cv2.getPerspectiveTransform(point1,point2)
imgwarped=cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow('output',img)
cv2.imshow('warped',imgwarped)
cv2.waitKey()