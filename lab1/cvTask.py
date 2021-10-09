import numpy as np
import cv2
# Code adapted from video camera, changing colorspaces, and contour features tutorial
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Convert BGR to RGB
    #rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # define range of blue color in rgb
    #lower_blue = np.array([0,0,0])
    #upper_blue = np.array([0,0,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)


    blue_obj, hierarchy = cv2.findContours(mask, 1, 2)
    if len(blue_obj) > 0:
        biggest_blue = max(blue_obj, key = cv2.contourArea) # used to find biggest blue contour, found example usage here: https://stackoverflow.com/questions/44588279/find-and-draw-the-largest-contour-in-opencv-on-a-specific-color-python
        
        # rect = cv2.minAreaRect(biggest_blue)
        # box = cv2.boxPoints(rect)
        # box = np.int0(box)
        # cv2.drawContours(frame, [box],0,(0,255,0),2)



        # fixed rectangle
        (x,y,w,h) = cv2.boundingRect(biggest_blue)
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()