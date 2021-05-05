import cv2 as cv

#respects aspect ratio
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)


img = cv.imread("images/LeBron_James_crop.jpg")
img = rescaleFrame(img)

cv.imshow("Lebron James",img);
cv.waitKey(0);

capture = cv.VideoCapture("videos/Component3.mp4");
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video',frame_resized)
    
    if cv.waitKey(20) & 0xFF==ord("d"):
        break
capture.release()
cv.destroyAllWindows()