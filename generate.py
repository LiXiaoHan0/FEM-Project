# 生成网格控制数据
file = open('input.txt',mode='w')

# 输出结点控制信息
# 结点号 x坐标 y坐标
file.write('65\n')
for x in range(13):
    for y in range(5):
        file.write('{} {} {}\n'.format(5*x+y+1,x,y))

# 输出连杆控制信息
# 结点1 结点2
file.write('160\n')
for x in range(12): # x方向杆
    for y in range(5):
        file.write('{} {}\n'.format(5*x+y+1,5*x+y+6))

for x in range(13): # y方向杆
    for y in range(4):
        file.write('{} {}\n'.format(5*x+y+1,5*x+y+2))

for x in range(12): # 斜拉杆
    for y in range(4):
        file.write('{} {}\n'.format(5*x+y+2,5*x+y+6))

# 输出边界条件
# 结点号 x方向位移 y方向位移
file.write('2\n')
file.write('1 0 0\n')
file.write('61 0 0\n')
        
# 输出外荷载条件
# 节点号 x方向集中力 y方向集中力
file.write('1\n')
file.write('21 0 1000000\n')

file.close()