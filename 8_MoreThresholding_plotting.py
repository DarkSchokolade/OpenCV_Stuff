import cv2
import matplotlib.pyplot as plt

img = cv2.imread('gradient.png')

ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, th3 = cv2.threshold(img, 50, 255, cv2.THRESH_TRUNC)
ret, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

# ret, th6 = cv2.threshold(img, 127, 255, cv2.THRESH_OTSU)

titles = ['original', 'BINARY', 'BINARY INVERSE', 'TRUNC', 'TOZERO', 'TOZERO_INV']
image = [img, th1, th2, th3, th4, th5]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(image[i], 'gray')    # subplot(rows, colums, start index)
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

# cv2.imshow('original', img)
# cv2.imshow('th1', th1)
# cv2.imshow('th2', th2)
# cv2.imshow('th3', th3)
# cv2.imshow('th4', th4)
# cv2.imshow('th5', th5)

# cv2.imshow('th6', th6)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
