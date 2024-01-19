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

+ main.py：主程序
+ model.py：类定义
+ element.py：单元分解
+ generate.py：数据生成
+ input.txt：网格剖分、边界条件、外部荷载数据
+ test.txt：测试数据，与课上ppt最后的实例一致
+ requirements.txt：环境配置文件

## 子任务

### 1.绘制剖分网格图

详见task.py中的preprocess函数

### 2.绘制后处理图

详见task.py中的postprocess函数