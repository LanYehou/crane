import cv2 as cv
import numpy as np

def get_hsv_demo(src_im):#色彩模型转换，BGR2HSV
    hsv = cv.cvtColor(src_im,cv.COLOR_BGR2HSV)
    return (hsv)


def hist2d_demo(src_hsv):#直方图
    hist = cv.calcHist([src_hsv],[0,1],None,[32,32],[0,180,0,256])#生成直方图
    return (hist)


def back_projection_demo(hist_sample,hsv_target):#直方图反向投影
    cv.normalize(hist_sample,hist_sample,0,255,cv.NORM_MINMAX)
    dst = cv.calcBackProject([hsv_target],[0,1],hist_sample,[0,180,0,256],1)
    return (dst)


def template_demo(tpl,target):#模板匹配
    method = [cv.TM_SQDIFF_NORMED]
    th , tw = tpl.shape[:2]
    result = cv.matchTemplate(target,tpl,method[0])
    min_val,max_val,min_loc,max_loc = cv.minMaxLoc(result)
    tl = min_loc
    br = (tl[0]+tw,tl[1]+th)
    return (cv.rectangle(target,tl,br,(0,0,200),2))


def contours_demo(src_im):#轮廓检测
    src_blur = cv.GaussianBlur(src_im,(3,3),0)#高斯模糊
    src_gray = cv.cvtColor(src_blur,cv.COLOR_BGR2GRAY)
    ret,src_binary = cv.threshold(src_gray,0,255,cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imshow("b", src_binary)
    contours,heriachy = cv.findContours(src_binary,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    for i , contour in enumerate(contours):
        cv.drawContours(src_im,contours,i,(0,0,255),2)
    return (src_im)


if __name__ == "__main__" :
    path_im1 = 'images/red.jpg'
    path_im2 = 'images/target.jpg'
    src_im1 = cv.imread(path_im1)
    src_im2 = cv.imread(path_im2)
    hsv = get_hsv_demo(src_im1)
    hsv2 = get_hsv_demo(src_im2)
    hist = hist2d_demo(hsv)
    dst = back_projection_demo(hist,hsv2)
    cv.imshow('dst',dst)
    #cv.imwrite('images/download_im.jpg',dst)
    cv.imshow('dst1',contours_demo(src_im2))
    tpl = cv.imread('images/sample.jpg')
    target = cv.imread('images/download_im.jpg')
    output = template_demo(tpl,target)
    #cv.imwrite('images/output1.jpg',output)
    cv.imshow('output',output)
    cv.waitKey(0)
    cv.destroyAllWindows()
