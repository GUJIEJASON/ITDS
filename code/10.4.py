import numpy as np

# 定义矩阵A（示例矩阵）
A = np.array([[2, 1],
              [4, 5]])

# 设置初始向量
v = np.random.rand(A.shape[0])  # 随机生成一个初始向量
v = v / np.linalg.norm(v)  # 规范化初始向量

# 设定迭代次数和容忍误差
max_iterations = 1000
tolerance = 1e-6

for i in range(max_iterations):
    Av = np.dot(A, v)  # 计算Av
    eigenvalue = np.dot(v, Av)  # 估算特征值

    v = Av / np.linalg.norm(Av)  # 规范化v

    if np.linalg.norm(Av - eigenvalue * v) < tolerance:
        break

print("估算的最大特征值:", eigenvalue)
print("对应的特征向量:", v)
