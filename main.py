import numpy as np
from model import point,element
from task import preprocess,postprocess

######################### 数据读入 #########################

points=[] # 结点数据
file = open('input.txt',mode='r')
n=int(file.readline())
for i in range(n):
    data=list(map(int,file.readline().split(' ')))
    points.append(point(*data))

# 连杆条件
m=int(file.readline())
for i in range(m):
    data=list(map(int,file.readline().split(' ')))
    points[data[0]].links.append[data[1]]
    points[data[1]].links.append[data[2]]

borders=[] # 边界条件
l=int(file.readline())
for i in range(l):
    data=list(map(int,file.readline().split(' ')))
    borders.append(data)

forces=[] # 外力荷载
s=int(file.readline())
for i in range(s):
    data=list(map(int,file.readline().split(' ')))
    forces.append(data)

file.close()

######################### 单元分解 #########################
elements=[]


######################### 整体分析 #########################


######################### 数据输出 #########################

