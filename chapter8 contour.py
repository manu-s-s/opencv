import cv2
import numpy as np

cap=cv2.VideoCapture(0)

lower_green = np.array([22, 44, 22])
upper_green = np.array([99, 213, 186])
while True:

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask_created = cv2.inRange(hsv, lower_green, upper_green)
    result = cv2.bitwise_and(frame,frame,mask=mask_created)

    contours,_=cv2.findContours(mask_created,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    
    for contour in contours:
        if cv2.contourArea(contour)>500:
            cv2.drawContours(frame,contour,-1,(0,250,0),3)

    
    cv2.imshow("frame", frame)
    cv2.imshow("mask created", mask_created)
    cv2.imshow("result", result)

    if cv2.waitKey(1)==27: 
        break 