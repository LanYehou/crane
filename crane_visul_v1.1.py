import cv2 as cv
import numpy as np

def get_hsv_demo(src_im):#色彩模型转换，BGR2HSV
    hsv = cv.cvtColor(src_im,cv.COLOR_BGR2HSV)
    return (hsv)

def get_mask(hsv):
    lower = np.array([150,50,80])
    higher = np.array([255,100,150])
    mask = cv.inRange(hsv,lowerb=lower,upperb=higher)

    return mask

def bitwise_and_demo(src_im,hsv):

    dst = cv.bitwise_and(src_im,src_im, mask=get_mask(hsv))
    cv.imshow("dst",dst)
    dst = cv.cvtColor(dst, cv.COLOR_HSV2BGR)
    dst = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)

    ret, src_binary = cv.threshold(dst, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    return src_binary

def video_demo():
    capture = cv.VideoCapture(1)
    while(True):
        ret,frame = capture.read()
        frame = cv.GaussianBlur(frame,(5,5),0)
        dst = bitwise_and_demo(frame,get_hsv_demo(frame))
        s = measure_object(dst)
        cv.imshow("video",s)
        cv.imshow("video_o", frame)
        c = cv.waitKey(50)
        if c == 27 :
            break
def measure_object(src_im):

    try:
        contours, heriachy = cv.findContours(src_binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        for i, contour in enumerate(contours):
            mm = cv.moments(contour)  #计算几何中心
            cx = mm['m10']/mm['m00']
            cy = mm['m01']/mm['m00']
            print (int(cx),int(cy))
            cv.circle(src_im,(int(cx),int(cy)),3,(0,255,255),-1)
        return (src_im)
    except: return (src_im)

video_demo()