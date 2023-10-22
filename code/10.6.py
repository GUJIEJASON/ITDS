import numpy as np

# 示例数据集，每一列代表一个特征，每一行代表一个观测值
cov_matrix = np.array([[1, -1, 4],
                 [2, 1, 3],
                 [1, 3, -1]])

# 设置迭代参数
max_iterations = 100
tolerance = 1e-6

# 初始化随机向量
n = cov_matrix.shape[0]
eigenvalues = []  # 存储特征值
eigenvectors = []  # 存储特征向量

for _ in range(n):
    v = np.random.rand(n)

    for i in range(max_iterations):
        # 迭代幂迭代方法
        v_new = np.dot(cov_matrix, v)
        eigenvalue = np.linalg.norm(v_new)  # 估计特征值
        v_new = v_new / eigenvalue  # 标准化向量

        # 计算收敛性
        if np.linalg.norm(v - v_new) < tolerance:
            break

        v = v_new

    # 存储估计的特征值和特征向量
    eigenvalues.append(eigenvalue)
    eigenvectors.append(v)

# 打印估计的特征值和特征向量
print("Estimated Eigenvalues:")
print(eigenvalues)
print("\nEstimated Eigenvectors:")
print(eigenvectors)
