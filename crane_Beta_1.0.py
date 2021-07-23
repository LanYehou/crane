'''
version: Beta 1.0；
暂时只能识别蓝色图形；
基于OpenCV numpy；
先提取出蓝色区域，找到最大的轮廓，并返回此轮廓的位置；
通过算法找识别灰度图像中的图形，返回图形的位置和种类；
对比蓝色轮廓位置和图形位置，如果位置接近则可知是蓝色的某种形状；
'''
import cv2 as cv
import numpy as np

blue_lower = np.array([100, 60, 60])
blue_upper = np.array([124, 255, 255])
red_lower = np.array([60, 60, 100])
red_upper = np.array([255, 255, 124])

def get_color(lower,upper):
    ret, frame = cap.read()
    frame = cv.GaussianBlur(frame, (5, 5), 0)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, lower, upper)
    # 图像学膨胀腐蚀
    mask = cv.erode(mask, None, iterations=2)
    mask = cv.GaussianBlur(mask, (3, 3), 0)
    res = cv.bitwise_and(frame, frame, mask=mask)
    # 寻找轮廓
    cnts = cv.findContours(mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[-2]

    if len(cnts) > 0:
        # 寻找面积最大的轮廓
        cnt = max(cnts, key=cv.contourArea)
        (x, y), radius = cv.minEnclosingCircle(cnt)
        #cv.circle(frame, (int(x), int(y)), int(radius), (255, 0, 255), 2)
        # 找到物体的位置坐标,获得颜色物体的位置
        return (int(x), int(y))
    else:
        pass


def find_circles():
    ret,frame=cap.read()
    frame = cv.GaussianBlur(frame, (5, 5), 0)
    gray = cv.cvtColor(frame, cv.COLOR_RGBA2GRAY)
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 20, param1=100, param2=45, minRadius=0, maxRadius=0)
    if str(circles) != 'None':
        return (int(circles[0][0][0]),int(circles[0][0][1]))

    else:
        return (0,0)

def find_triangel():
    ret, frame = cap.read()
    frame = cv.GaussianBlur(frame, (5, 5), 0)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, blue_lower, blue_upper)
    # 图像学膨胀腐蚀
    mask = cv.erode(mask, None, iterations=2)
    mask = cv.GaussianBlur(mask, (3, 3), 0)
    #res = cv.bitwise_and(frame, frame, mask=mask)
    # 寻找轮廓
    cnts = cv.findContours(mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[-2]

    if len(cnts) > 0:
        # 寻找面积最大的轮廓
        cnt = max(cnts, key=cv.contourArea)
        (x, y), radius = cv.minEnclosingCircle(cnt)


        approxCurve = cv.approxPolyDP(cnt, 4, True)
        if approxCurve.shape[0] == 4:
            return (x,y,'rectangel')
        elif approxCurve.shape[0] == 3:
            return (x,y,'triangel')
        else:
            return (0,0,'none')
    else:
        pass

cap = cv.VideoCapture(0)
cap.set(3, 320)
while 1 :
    blue_x,blue_y=get_color(blue_lower,blue_upper)
    #red_x,red_y=get_color(red_lower,red_upper)
    circles_x,circles_y=find_circles()
    if circles_x != 0 and circles_y !=0 :
        if blue_x < circles_x+30 and blue_x > circles_x-30:
            print('bluecircle')
        #elif red_x < circles_x+30 and red_x > circles_x-30:
            #print('redcircle')
        else:
            pass
    else:
        blue_x, blue_y = get_color(blue_lower, blue_upper)
        x,y,shape=find_triangel()
        if x != 0 and y != 0:
            if blue_x < x + 30 and blue_x > x - 30:
                print('blue'+shape)
            # elif red_x < circles_x+30 and red_x > circles_x-30:
            # print('redcircle')
            else:
                pass


    if cv.waitKey(5) & 0xFF == 27:
        break
cap.release()
