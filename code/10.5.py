import numpy as np

# 示例数据集，每一列代表一个特征，每一行代表一个观测值
data = np.array([[1, -1, 4],
                 [2, 1, 3],
                 [1, 3, -1]])

# 计算协方差矩阵
cov_matrix = np.cov(data, rowvar=False)

# 输出协方差矩阵
print("协方差矩阵:")
print(cov_matrix)
