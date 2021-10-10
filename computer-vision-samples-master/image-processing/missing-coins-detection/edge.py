import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('blackandwhite.jpg',0)
edges=cv2.Canny(img,100,200)

f,axarr=plt.subplots(1,2)


axarr[0].imshow(img,cmap='gray'),axarr[0].axis('off'),axarr[0].set_title('image')
axarr[1].imshow(edges,cmap='gray'),axarr[1].axis('off'),axarr[1].set_title('edges')
plt.show()