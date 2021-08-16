'''
version: Beta 1.1；
基于OpenCV numpy；

主程序流程：
先提取红色轮廓 handle_img(red_lower,red_upper)；
提取到了：
    获取面积最大的轮廓的位置 get_color()；
    识别此轮廓是否为圆 find_circles()：
    如果不是圆：
        识别是否为多边形 find_polygon()；
没提取到：
    提取蓝色轮廓 handle_img(blue_lower,blue_upper)；
        提取到了：
            获取面积最大的轮廓的位置 get_color()；
            识别此轮廓是否为圆 find_circles()：
            如果不是圆：
                识别是否为多边形 find_polygon()；
        没提取到：
            pass；

优化项目：
简化了识别流程；
优化了程序结构
减少了Opencv函数调用次数；
解决了没有识别到任何颜色轮廓时会报错的bug；
去除了位置比对过程；

待优化：
红色的颜色范围不准确；
'''

import cv2 as cv
import numpy as np
from collections import Counter

blue_lower = np.array([100, 130, 60]) # 蓝色范围，最低值
blue_upper = np.array([124, 255, 255]) # 蓝色范围，最高值
red_lower = np.array([125, 0, 70]) # 红色范围，最低值
red_upper = np.array([179, 255, 255]) # 红色范围，最高值


def handle_img(lower,upper):
    global cnts

    mask = cv.inRange(hsv, lower, upper)

    # 图像学膨胀腐蚀
    mask = cv.erode(mask, None, iterations=2)
    mask = cv.GaussianBlur(mask, (3, 3), 0)
    # 寻找轮廓
    cnts = cv.findContours(mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[-2]


def get_color():
    if len(cnts) > 0:
        # 寻找面积最大的轮廓
        global cnt
        cnt = max(cnts, key=cv.contourArea)
        (x, y), radius = cv.minEnclosingCircle(cnt)
        # 获取轮廓位置
        return (int(x), int(y))
    else:
        return (0,0)


def find_circles():
    gray = cv.cvtColor(frame, cv.COLOR_RGBA2GRAY)
    # 霍夫圆检测
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 20, param1=100, param2=70, minRadius=0, maxRadius=0)
    if str(circles) != 'None':
        return (int(circles[0][0][0]),int(circles[0][0][1]))
    else:
        return (0,0)


def find_polygon():
    (x, y), radius = cv.minEnclosingCircle(cnt)
    approxCurve = cv.approxPolyDP(cnt, 4, True)
    if approxCurve.shape[0] == 4:
        return (x,y,'rectangel')
    elif approxCurve.shape[0] == 3:
        return (x,y,'triangel')
    else:
        return (0,0,'none')




def get_boxtype():
    global frame
    global hsv
    shape=[]
    cap = cv.VideoCapture(1)
    times=0

    while times<20:
        times = times + 1
        ret, frame = cap.read()
        frame = cv.GaussianBlur(frame, (5, 5), 0)
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        handle_img(red_lower,red_upper)
        color_x,color_y=get_color()
        if color_x != 0 :
            cricle_x,cricle_y=find_circles()
            if cricle_x != 0:
                shape.append('redcricle')
                x = cricle_x
                y = cricle_y
            else:
                polygon_x,polygon_y,polygon_type=find_polygon()
                if polygon_type == 'rectangel' :
                    shape.append('red'+polygon_type)
                    x = polygon_x
                    y = polygon_y
                elif polygon_type  == 'triangel' :
                    shape.append('red'+polygon_type)
                    x = polygon_x
                    y = polygon_y
                else:
                    pass
        else:
            handle_img(blue_lower,blue_upper)
            color_x, color_y = get_color()
            if color_x != 0:
                cricle_x, cricle_y = find_circles()
                if cricle_x != 0:
                    shape.append('bluecricle')
                    x = cricle_x
                    y = cricle_y
                else:
                    polygon_x, polygon_y, polygon_type = find_polygon()
                    if polygon_type == 'rectangel':
                        shape.append('blue' + polygon_type)
                        x = polygon_x
                        y = polygon_y
                    elif polygon_type == 'triangel':
                        shape.append('blue' + polygon_type)
                        x = polygon_x
                        y = polygon_y
                    else:
                        pass
            else:
                pass
    cap.release()
    collection_shape = Counter(shape)
    most_counterNum = collection_shape.most_common(1)
    return (most_counterNum[0][0],x,y)


