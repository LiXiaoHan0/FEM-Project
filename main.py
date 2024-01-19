import numpy as np
from model import point,element
from task import preprocess,postprocess

######################### 数据读入 #########################
file = open('input.txt',mode='r')

points=[] # 结点数据
n=int(file.readline())
for i in range(n):
    data=list(map(int,file.readline().split(' ')))
    points.append(point(*data))

sticks=[] # 连杆条件
for i in range(int(file.readline())):
    data=list(map(int,file.readline().split(' ')))
    sticks.append(data)
    points[data[0]].links.append(data[1])
    points[data[1]].links.append(data[0])

borders=[] # 边界条件
for i in range(int(file.readline())):
    data=list(map(int,file.readline().split(' ')))
    borders.append(data)

forces=[] # 外力荷载
for i in range(int(file.readline())):
    data=list(map(int,file.readline().split(' ')))
    forces.append(data)

file.close()

######################### 单元分解 #########################
elements=[]
for pp in points:
    for ss in sticks:
        if(pp.num>=ss[0] or pp.num>=ss[1]):continue
        if(ss[0] in pp.links and ss[1] in pp.links):
            elements.append(element(len(elements),pp,points[ss[0]],points[ss[1]]))

# for i in elements:
#     print(i.num,i.p[0].num,i.p[1].num,i.p[2].num)

# 绘制网格剖分图
preprocess(points,sticks,elements)

######################### 整体分析 #########################
K=np.zeros((2*n,2*n)) # 整体刚度矩阵
for ee in elements:
    G=np.zeros((6,2*n))
    for t in range(3):
        i=ee.p[t].num
        G[2*t][2*i]=1
        G[2*t+1][2*i+1]=1
    K=K+np.dot(np.dot(G.T,ee.K),G)

P=np.zeros((2*n,1)) # 整体荷载向量
for ff in forces:
    P[2*ff[0]][0]=ff[1]
    P[2*ff[0]+1][0]=ff[2]

# 引入边界条件
for bb in borders:
    for t in range(2):
        if(bb[t+1]==0):
            i=2*bb[0]+t
            P[i][0]=0
            for j in range(2*n):
                K[j][i]=0
                K[i][j]=0
            K[i][i]=1

# 求解线性方程组
ans=np.linalg.solve(K,P)
for i in range(n):
    points[i].move(ans[2*i][0],ans[2*i+1][0])

# 绘制应力/应变等值线图
postprocess(points)