import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('tray-of-coins.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

box_mask = cv2.inRange(hsv, np.array([0,90,190]), np.array([180,255,255]))

f,axarr=plt.subplots(2,3)

box_mask = cv2.bitwise_not(box_mask)
box_mask = cv2.medianBlur(box_mask, 15)
axarr[0,0].imshow(box_mask,cmap='gray'),axarr[0,0].axis('off'),axarr[0,0].set_title('box mask')

coin_mask = cv2.inRange(hsv, np.array([5, 0, 0]), np.array([170, 255, 255]))
coin_mask = cv2.medianBlur(coin_mask, 25)
axarr[0,1].imshow(coin_mask,cmap='gray'),axarr[0,1].axis('off'),axarr[0,1].set_title('coin_mask')

contours, hierarchies = cv2.findContours(coin_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#print (str(len(contours)) + ' boxes found')
i=1
for con in contours:
    if i!=24:
        M = cv2.moments(con) 
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        h, w = box_mask.shape
        cv2.circle(img,(cX, cY),20,(125,0,250),7)
        cv2.putText(img,f'{i}',(cX,cY), cv2.FONT_HERSHEY_SIMPLEX, 4,(255,0,255),2,-1)
        cv2.floodFill(box_mask, None, (cX,cY), 0)
        i+=1

axarr[0,2].imshow(box_mask,cmap='gray'),axarr[0,2].axis('off'),axarr[0,2].set_title('box_mask after floodfill')

final_contours, _ = cv2.findContours(box_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

box_with_contours=cv2.cvtColor(box_mask,cv2.COLOR_GRAY2BGR)

cv2.drawContours(box_with_contours,final_contours,-1,(0,250,0),-1) # look at the green dot at the top

# print(set(tuple(v) for m2d in box_with_contours for v in m2d)) "to get all colors"
axarr[1,0].imshow(box_with_contours),axarr[1,0].axis('off'),axarr[1,0].set_title('box_with_contours')

missing = 0
for con in final_contours:
    x,y,w,h = cv2.boundingRect(con)
    if y!=0:
        missing += 1
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,250),50)
# print (str(missing) + ' coins missing')

cv2.putText(img,'Missing:' + str(missing),(10,100), cv2.FONT_HERSHEY_SIMPLEX, 4,(255,255,255),10,-1)
axarr[1,1].imshow(img),axarr[1,1].axis('off'),axarr[1,1].set_title('img')

axarr[1,2].axis('off')

plt.show()
