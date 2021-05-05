import cv2 as cv

#reading of an image
img = cv.imread("images/LeBron_James_crop.jpg")
print(img.shape)
cv.imshow("Lebron James",img)
cv.waitKey(0)

#convert to greyscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)
cv.waitKey(0)

#blur
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)
cv.waitKey(0)

#Edge Cascade
canny = cv.Canny(blur,125,175)
cv.imshow("Edges", canny)
cv.waitKey(0)

#Dilute image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow("Dilated",dilated)
cv.waitKey(0)

#Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded',eroded)
cv.waitKey(0)

#Resize without regard of aspect ratio
resized = cv.resize(img,(500,500))
cv.imshow('Resized',resized)
cv.waitKey(0)

#cropping
cropped = img[50:200, 200:400]
cv.imshow("Cropped",cropped)
cv.waitKey(0)

