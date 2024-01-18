# FEM-Project

结构分析有限元大作业

## 快速上手

直接下载或执行以下代码

```bash
git clone git@github.com:LiXiaoHan0/FEM-Project.git
```

若要完整运行主程序，请先执行以下代码创建环境

```bash
conda create -n structure python=3.8.12
conda activate structure
pip install -r requirements.txt
```

## 目录结构

+ main.py：主程序文件
+ model.py：类定义文件
+ test.py：测试文件
+ input.txt：网格剖分、边界条件、外部荷载数据
+ requirements.txt：环境配置文件

## 子任务

### 1.绘制剖分网格图

+ 输入：网格剖分信息
  + input.txt，格式如下
    + 第1行，一个整数，表示结点数量n
    + 接下来n行，每行3个整数，分别表示结点码、结点x坐标、结点y坐标
    + 接下来1行，一个整数，表示连杆数量m
    + 接下来m行，每行2个整数，分别表示连杆两端的结点号
    + 其余若干行，边界条件及外部荷载数据，可忽略
  + cell.txt，格式如下
    + 第一行，一个整数，表示单元数量k
    + 接下来k行，每行4个整数，分别为单元码、单元三个端点的结点码
+ 输出：网格剖分示意图，需包含结点码和单元码

### 2.绘制后处理图

