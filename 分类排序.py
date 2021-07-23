import random

Shape={'triangle':'三角形','circle':'圆形','square':'方形'}
Color={'blue':'蓝色','red':'红色'}#蓝下红上,先拿红色
MyExample=[['triangle','blue'],['triangle','red'],['circle','blue'],['circle','red'],
           ['square','blue'],['square','red']]

def Example():#生成例子
    ChoiceExample=random.sample(MyExample,6)
    # print(ChoiceExample)
    return ChoiceExample
OldColumn={}
for example_num,OneExample in zip(range(6),Example()):
    OldColumn[example_num]=OneExample
# print(OldColumn)
triangle= {}
circle= {}
square= {}
for num,oneExampe in zip(range(6),OldColumn.values()):
    # print(num,oneExampe)
    if oneExampe[0]=='triangle':
        triangle[oneExampe[1]]=num
    if oneExampe[0]=='circle':
        circle[oneExampe[1]]=num
    if oneExampe[0] == 'square':
        square[oneExampe[1]]=num
print('triangle',triangle)
print('circle',circle)
print('square',square)
#搬运三角形
print('先取三角形红色')
print('物料区第'+str(triangle['red'])+'个')
print('再取三角形蓝色')
print('物料区第'+str(triangle['blue'])+'个')
#搬运圆形
print('先取圆形红色')
print('物料区第'+str(circle['red'])+'个')
print('再取圆形蓝色')
print('物料区第'+str(circle['blue'])+'个')
#搬运方形
print('先取方形红色')
print('物料区第'+str(square['red'])+'个')
print('再取方形蓝色')
print('物料区第'+str(square['blue'])+'个')