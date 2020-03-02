import cv2

img = cv2.imread('lena.jpg',1)
img = cv2.line(img,(0,0),(255,225),(200,255,7),6)
img = cv2.arrowedLine(img,(0,300),(300,300),(0,5,6),8)  # color is in bgr format

img=cv2.rectangle(img,(250,2),(300,300),(0,200,0),-1)

font = cv2.FONT_HERSHEY_TRIPLEX
img = cv2.putText(img , 'wrryyyy' , (10, 500) , font, 3, (0,250,250),10,cv2.LINE_AA)

cv2.imshow('opencv image thingy',img)

cv2.waitKey(0)
cv2.destroyAllWindows()