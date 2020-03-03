import numpy as np
import cv2

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)


def click_event(event, x, y, flags, parm):

    # Left Button Event
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,', ', y)
        font = cv2.FONT_HERSHEY_PLAIN
        strxy = str(x)+ ', ' + str(y)
        cv2.putText(img, strxy, (x, y), font, 1, (255,255,0), 2)
        cv2.imshow('image', img)

    # Right Button Event
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        font1 = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        strBGR = str(blue)+','+str(green)+','+str(red)
        cv2.putText(img,strBGR, (x,y), font1, 0.5, (0,255,250), 2)
        cv2.imshow('image', img)


# img = np.zeros((512, 512,  3), np.uint8)
img = cv2.imread('lena.jpg')
cv2.imshow('image', img)

cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()