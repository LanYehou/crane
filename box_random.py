import numpy as np
Shape={'triangle':'三角形','circle':'圆形','square':'方形'}
Color={'blue':'蓝色','red':'红色'}#蓝下红上,先拿红色
MyExample=[['triangle','blue'],['triangle','red'],['circle','blue'],['circle','red'],
           ['square','blue'],['square','red']]
transportedbox = 0
np.random.shuffle(MyExample)#对盒子进行随机排序
print(MyExample)
while transportedbox <= 5 :
    i = 0
    while i < 5-transportedbox:#循环，找一个红色的盒子
        if MyExample[i][1]== 'red' :
            tmpShape = MyExample[i][0]#保存盒子的形状
            print('taked',MyExample[i])
            del MyExample[i]#删除已经拿了的盒子
            transportedbox = transportedbox+1
            break
        i = i+1
    n = 0
    while n < 5 - transportedbox:
        if MyExample[n][0] == tmpShape :#找一个和刚刚拿的盒子形状一样的盒子
            print('2taked',MyExample[n])
            print('transported')
            del MyExample[n]
            leftbox = transportedbox+1
            break
        n = n+1