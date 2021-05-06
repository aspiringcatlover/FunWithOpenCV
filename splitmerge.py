import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("images/LeBron_James_crop.jpg")
cv.imshow("Lebron James",img)

blank = np.zeros(img.shape[:2],dtype='uint8')


#split image into 3 bgr color channel images
b,g,r = cv.split(img)

b = cv.merge([b,blank,blank])
g = cv.merge([blank,g,blank])
r = cv.merge([blank,blank,r])


cv.imshow("b",b)
cv.imshow("g",g)
cv.imshow("r",r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

cv.waitKey(0)
