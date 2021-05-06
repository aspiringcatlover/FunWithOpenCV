import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("images/LeBron_James_crop.jpg")
cv.imshow("Lebron James",img)

#bgr to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

#bgr to hsv
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("HSV",hsv)

#bgr to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB",lab)

#bgr to rgb
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB",rgb)
plt.imshow(rgb)
plt.show()
cv.waitKey(0)
