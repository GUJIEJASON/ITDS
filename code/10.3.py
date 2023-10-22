import numpy as np

# 创建一个示例矩阵
A = np.array([[2, 1],
              [4, 5]])

# 使用 numpy.linalg.eig 计算特征值和特征向量
eigenvalues, eigenvectors = np.linalg.eig(A)

# 特征值
print("特征值:")
print(eigenvalues)

# 特征向量
print("特征向量:")
print(eigenvectors)
