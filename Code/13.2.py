from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# 导入鸢尾花数据集
iris = load_iris()
X = iris.data  # 特征数据
y = iris.target  # 目标标签

# 使用train_test_split方法进行切分
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# test_size参数指定了测试集的比例，这里设置为0.2表示20%的数据用于测试。
# random_state参数可选，它可以用来设置随机数生成的种子，以确保切分结果的可重现性。

# 打印训练集和测试集的形状
print("训练集特征数据形状:", X_train.shape)
print("测试集特征数据形状:", X_test.shape)
print("训练集目标标签形状:", y_train.shape)
print("测试集目标标签形状:", y_test.shape)
