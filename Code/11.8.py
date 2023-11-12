import numpy as np
from sklearn.datasets import load_iris
from sklearn.metrics import euclidean_distances

# 加载鸢尾花数据集
data = load_iris()
X = data.data
y = data.target

# 获取唯一的类别标签
unique_labels = np.unique(y)

# 初始化字典来存储每个类别的中心点
class_centers = {}

# 计算每个类别的中心点
for label in unique_labels:
    class_centers[label] = np.mean(X[y == label], axis=0)

# 输出每个类别的中心点
for label, center in class_centers.items():
    print(f'中心点标签 {label}: {center}')

# 计算数据点到中心点的欧式距离
distances = euclidean_distances(X, [class_centers[label] for label in y])

# 输出每个数据点到中心点的欧式距离
for i, label in enumerate(y):
    print(f'数据点 {i} 到中心点 {label} 的欧式距离: {distances[i, label]}')
