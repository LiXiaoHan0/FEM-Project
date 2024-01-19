import numpy as np

t=1 # 不妨假设单元厚度为1m
E=28000000000
v=0.2

# 测试数据
# E=1
# v=0

# 计算弹性矩阵
D=E/(1-v*v)*np.array([[1,v,0],[v,1,0],[0,0,(1-v)/2]])

class point():
    
    def __init__(self,num=0,x=0,y=0):
        self.num=num
        self.x=x
        self.y=y
        self.links=[]

    def move(self,u,v):
        self.u=u
        self.v=v

class element():

    # 初始化单元属性
    def __init__(self,num=0,p1=point(),p2=point(),p3=point()):
        self.num=num
        self.p=[p1,p2,p3]
    
    # 计算面积
    def __A(self):
        x1=self.p[1].x-self.p[0].x
        y1=self.p[1].y-self.p[0].y
        x2=self.p[2].x-self.p[0].x
        y2=self.p[2].y-self.p[0].y
        return abs(x1*y2-x2*y1)/2

    # 计算应变子矩阵
    def __matrix_B(self,i): 
        j=(i+1)%3
        k=(j+1)%3
        b=self.p[j].y-self.p[k].y
        c=self.p[k].x-self.p[j].x
        return np.array([[b,0],[0,c],[c,b]])
    
    # 计算单元刚度矩阵
    def matrix_K(self):
        A=self.__A()
        B=np.column_stack((self.__matrix_B(0),self.__matrix_B(1),self.__matrix_B(2)))/2/A
        K=np.dot(np.dot(B.T,D),B)*t*A
        return K
