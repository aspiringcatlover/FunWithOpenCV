import cv2 as cv

#reading of an image
img = cv.imread("images/LeBron_James_crop.jpg")
cv.imshow("Lebron James",img);
cv.waitKey(0);

#reading of video
capture = cv.VideoCapture("videos/Component3.mp4");
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)
    
    if cv.waitKey(20) & 0xFF==ord("d"):
        break
capture.release()
cv.destroyAllWindows()