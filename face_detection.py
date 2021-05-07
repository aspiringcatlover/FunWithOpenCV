import cv2 as cv


img = cv.imread("images/LeBron_James_crop.jpg")
cv.imshow("Lebron James",img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Lebron James",gray)

haar_cascade = cv.CascadeClassifier('models/haar_face.xml')

#higher minNeighbour -> less false positive
face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7)

print(f'{len(face_rect)} faces found')

for (x,y,w,h) in face_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)
cv.imshow("Detected faces",img)
cv.waitKey(0)

#extendable to videos by analysing each frame instead of an image
