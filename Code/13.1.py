import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rc("font",family='YouYuan')
from sklearn import datasets

# 导入鸢尾花数据集
iris = datasets.load_iris()
X = iris.data  # 特征数据
y = iris.target  # 目标标签

# 可视化数据
# 以下示例可视化了鸢尾花数据集的前两个特征（花萼长度和花萼宽度）

# 创建散点图
plt.figure(figsize=(8, 6))
plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], label='Setosa', color='b', marker='o')
plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], label='Versicolor', color='g', marker='s')
plt.scatter(X[y == 2][:, 0], X[y == 2][:, 1], label='Virginica', color='r', marker='x')

# 添加标签和标题
plt.xlabel('花萼长度 (cm)')
plt.ylabel('花萼宽度 (cm)')
plt.title('鸢尾花数据集 - 花萼长度 vs. 花萼宽度')

# 添加图例
plt.legend(loc='upper left')

# 显示图表
plt.show()
