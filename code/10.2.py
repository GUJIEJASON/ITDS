import numpy as np
import matplotlib.pyplot as plt

# 生成服从标准正态分布的10000个样本
samples = np.random.randn(10000)

# 创建直方图
plt.hist(samples, bins=60, density=True, alpha=0.6, color='b')

# 添加标签和标题
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Standard Normal Distribution Samples')

# 展示图表
plt.show()
