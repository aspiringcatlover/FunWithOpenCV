import cv2 as cv

img = cv.imread("images/LeBron_James_crop.jpg")
cv.imshow("Lebron James",img)

#convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)


#simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Simple threshold", thresh)


#simple thresholding
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Simple threshold inversed", thresh_inv)

#adaptive thresholding
adaptive_threshold = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C,cv.
THRESH_BINARY, 11, 1)
cv.imshow("Adaptive threshold", adaptive_threshold)

cv.waitKey(0)