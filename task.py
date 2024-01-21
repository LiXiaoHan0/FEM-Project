import matplotlib.pyplot as plt 
import matplotlib.tri as mtri 
import numpy as np

# 前处理
# 输入为结点集、连杆集和单元集
# 输出为网格剖分示意图
def preprocess(points,sticks,elements):
    # 读取点、杆、元素数量
    p_len = len(points)
    s_len = len(sticks)
    e_len = len(elements)
    
    #绘制点图
    p_x = np.asarray([x.x for x in points])
    p_y = np.asarray([x.y for x in points])
    p_n = np.asarray([x.num for x in points])
    plt.scatter(p_x, p_y,c='r',zorder=3)
    #plt.text(p_x, p_y+0.3, '%.0f'%p_n, ha='center', va='bottom', fontsize=10.5,c='r')
    for i in range(p_len):
        plt.annotate('%.0f'%(i+1),(p_x[i],p_y[i]+0.02),fontsize=6)
        
    #绘制杆图
    s_x = [[p_x[[x[0]]],p_x[[x[1]]]] for x in sticks]
    s_y = [[p_y[[x[0]]],p_y[[x[1]]]] for x in sticks]
    for i in range(s_len):
        plt.plot(s_x[i], s_y[i], c='b')
        #plt.annotate('%.0f'%i,xy=((s_x[i][0]+s_x[i][1])/2, (s_y[i][0]+s_y[i][1])/2),xytext=(+15, -15))
    
    #绘制元素图,每一种颜色对应一个元素
    triangles = [[x.p[0].num,x.p[1].num,x.p[2].num] for x in elements]
    centroid_x = [(x.p[0].x+x.p[1].x+x.p[2].x)/3 for x in elements]
    centroid_y = [(x.p[0].y+x.p[1].y+x.p[2].y)/3 for x in elements]
    triang = mtri.Triangulation(p_x, p_y, triangles)
    colors = [x.num for x in elements]
    
    plt.tripcolor(triang, facecolors=colors, edgecolors='k',alpha=0.5,zorder=2)
    
    # 标记每个三角形序号
    for i, triangle in enumerate(triangles):
        plt.text(centroid_x[i], centroid_y[i], f' {i+1}', ha='center', va='center',color='red', fontsize=8)
    
    # 设置x和y坐标轴刻度为间隔为一
    plt.xticks(np.arange(np.floor(p_x.min()), np.ceil(p_x.max())+1, 1))
    plt.yticks(np.arange(np.floor(p_y.min()), np.ceil(p_y.max())+1, 1))
    plt.axis('equal')
    plt.show()
    
    return 0

# 后处理
# 输入为各个结点的坐标和位移和所计算的物理量编号
# 输出为应变或应力的云图
def postprocess(points,sticks,elements,process,mode):
    # 读取点、杆、元素数量
    p_len = len(points)
    s_len = len(sticks)
    e_len = len(elements)
    # 绘制点图
    p_x = np.asarray([x.x for x in points])
    p_y = np.asarray([x.y for x in points])
    p_n = np.asarray([x.num for x in points])
    plt.scatter(p_x, p_y, c='r', zorder=3)
    # plt.text(p_x, p_y+0.3, '%.0f'%p_n, ha='center', va='bottom', fontsize=10.5,c='r')
    for i in range(p_len):
        plt.annotate('%.0f' % (i + 1), (p_x[i], p_y[i] + 0.02), fontsize=6)

    # 绘制杆图
    s_x = [[p_x[[x[0]]], p_x[[x[1]]]] for x in sticks]
    s_y = [[p_y[[x[0]]], p_y[[x[1]]]] for x in sticks]
    for i in range(s_len):
        plt.plot(s_x[i], s_y[i], c='b')
        # plt.annotate('%.0f'%i,xy=((s_x[i][0]+s_x[i][1])/2, (s_y[i][0]+s_y[i][1])/2),xytext=(+15, -15))

    # 绘制应力应变云图，每个mode代表一个标量物理量
    triangles = [[x.p[0].num, x.p[1].num, x.p[2].num] for x in elements]
    triang = mtri.Triangulation(p_x, p_y, triangles)
    if mode==1:
      colors = [x.epislon[0][0] for x in process]
      print(colors)
      plt.tripcolor(triang, facecolors=colors, edgecolors='k', alpha=1,cmap='jet')
      plt.xticks(np.arange(np.floor(p_x.min()), np.ceil(p_x.max()) + 1, 1))
      plt.yticks(np.arange(np.floor(p_y.min()), np.ceil(p_y.max()) + 1, 1))
      plt.axis('equal')
      plt.colorbar()
      fig = plt.gcf()
      plt.show()
      fig.savefig('savefig_1.png')
    elif mode == 2:
        colors = [x.epislon[1][0] for x in process]
        plt.tripcolor(triang, facecolors=colors, edgecolors='k', alpha=1,cmap='jet')
        plt.xticks(np.arange(np.floor(p_x.min()), np.ceil(p_x.max()) + 1, 1))
        plt.yticks(np.arange(np.floor(p_y.min()), np.ceil(p_y.max()) + 1, 1))
        plt.axis('equal')
        plt.colorbar()
        fig = plt.gcf()
        plt.show()
        fig.savefig('savefig_2.png')
    elif mode == 3:
        colors = [x.epislon[2][0] for x in process]
        plt.tripcolor(triang, facecolors=colors, edgecolors='k', alpha=1,cmap='jet')
        plt.xticks(np.arange(np.floor(p_x.min()), np.ceil(p_x.max()) + 1, 1))
        plt.yticks(np.arange(np.floor(p_y.min()), np.ceil(p_y.max()) + 1, 1))
        plt.axis('equal')
        plt.colorbar()
        fig = plt.gcf()
        plt.show()
        fig.savefig('savefig_3.png')
    elif mode == 4:
        colors = [x.xigema[0][0] for x in process]
        plt.tripcolor(triang, facecolors=colors, edgecolors='k', alpha=1,cmap='jet')
        plt.xticks(np.arange(np.floor(p_x.min()), np.ceil(p_x.max()) + 1, 1))
        plt.yticks(np.arange(np.floor(p_y.min()), np.ceil(p_y.max()) + 1, 1))
        plt.axis('equal')
        plt.colorbar()
        fig = plt.gcf()
        plt.show()
        fig.savefig('savefig_4.png')
    elif mode == 5:
        colors = [x.xigema[1][0] for x in process]
        plt.tripcolor(triang, facecolors=colors, edgecolors='k', alpha=1,cmap='jet')
        plt.xticks(np.arange(np.floor(p_x.min()), np.ceil(p_x.max()) + 1, 1))
        plt.yticks(np.arange(np.floor(p_y.min()), np.ceil(p_y.max()) + 1, 1))
        plt.axis('equal')
        plt.colorbar()
        fig = plt.gcf()
        plt.show()
        fig.savefig('savefig_5.png')
    elif mode == 6:
        colors = [x.xigema[2][0] for x in process]
        plt.tripcolor(triang, facecolors=colors, edgecolors='k', alpha=1,cmap='jet')
        plt.xticks(np.arange(np.floor(p_x.min()), np.ceil(p_x.max()) + 1, 1))
        plt.yticks(np.arange(np.floor(p_y.min()), np.ceil(p_y.max()) + 1, 1))
        plt.axis('equal')
        plt.colorbar()
        fig = plt.gcf()
        plt.show()
        fig.savefig('savefig_6.png')
    return 0