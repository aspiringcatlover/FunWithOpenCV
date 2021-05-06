import cv2 as cv
import numpy as np

img = cv.imread("images/LeBron_James_crop.jpg")
cv.imshow("Lebron James",img)

#average blur
average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)

#gaussian blur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow("Gaussian Blur", gauss)

#median blur
median = cv.medianBlur(img,3)
cv.imshow("Median Blur", median)

#Bilateral blur
bi = cv.bilateralFilter(img, 5, 35,25)
cv.imshow("Bilateral Blur", bi)

cv.waitKey(0)