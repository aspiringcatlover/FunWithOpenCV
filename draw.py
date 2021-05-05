import cv2 as cv
import numpy as np

blank= np.zeros((500,500,3),dtype='uint8')

blank[:] = 0,255,255

#draws yellow blank image
cv.imshow("Yellow",blank)
cv.waitKey(0)


#draws rectangle
blank[:] = 0,0,0
cv.rectangle(blank,(0,0),(250,250), (0,0,255), thickness=-1)
cv.imshow('Rectangle', blank)
cv.waitKey(0)


#draws circle
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 50,(0,255,0),thickness=-1 )
cv.imshow('Circle', blank)
cv.waitKey(0)

#draws line
cv.line(blank, (blank.shape[1]//2,blank.shape[0]//2),(0,0),(255,255,255),thickness=2)
cv.imshow('Line', blank)
cv.waitKey(0)

#write text
cv.putText(blank, "Hello World", (150,150),cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0),2)
cv.imshow('Text', blank)
cv.waitKey(0)



#note opencv uses bgr instead of rgb by default