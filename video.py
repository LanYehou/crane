import cv2 as cv
def video_demo():
    capture = cv.VideoCapture(0)
    while(True):
        ret,frame = capture.read()
        cv.imshow("video",frame)
        c = cv.waitKey(50)
        if c == 27 :
            break

video_demo()
