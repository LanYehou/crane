import cv2 as cv
import numpy as np

def measure_object(src_im):
    src_gray = cv.cvtColor(src_im,cv.COLOR_BGR2GRAY)
    cv.imshow("src_gray", src_gray)
    ret, src_binary = cv.threshold(src_gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    #ret, src_binary = cv.threshold(src_gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("src_binary", src_binary)
    src_dst = cv.cvtColor(src_binary,cv.COLOR_GRAY2RGB)
    try:
        contours, heriachy = cv.findContours(src_binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        for i, contour in enumerate(contours):
            mm = cv.moments(contour)  #计算几何中心
            cx = mm['m10']/mm['m00']
            cy = mm['m01']/mm['m00']
            print (int(cx),int(cy))
            cv.circle(src_im,(int(cx),int(cy)),3,(0,255,255),-1)
            # cv.rectangle(src_im,(x,y),(x+w,y+h),(0,0,255),2)
            # approxCurve = cv.approxPolyDP(contour,4,True)
            # if approxCurve.shape[0] > 6 :
            #     cv.drawContours(src_im,contours,i,(255,0,255),2)
            # if approxCurve.shape[0] == 4:
            #     cv.drawContours(src_im, contours, i, (0, 255, 255), 2)
            # if approxCurve.shape[0] == 3:
            #     cv.drawContours(src_im, contours, i, (255, 255, 0), 2)
        #cv.imshow("out",src_im)
        return (src_im)
    except: return (src_im)


def video_demo():
    capture = cv.VideoCapture(1)
    while(True):
        ret,frame = capture.read()
        s = measure_object(frame)
        cv.imshow("video",s)
        c = cv.waitKey(50)
        if c == 27 :
            break

video_demo()