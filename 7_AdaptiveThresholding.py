import cv2

img = cv2.imread('bookpage.png', 0) # convert to black and white otherwise it wont work
_, th1 = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow('sudoku', img)
cv2.imshow('sudoku th', th1)
cv2.imshow('adaptive threshold', th2)
cv2.imshow('adaptive threshold gaussian', th3)

cv2.waitKey(0)
cv2.destroyAllWindows()