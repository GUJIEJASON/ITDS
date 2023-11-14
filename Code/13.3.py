from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 导入鸢尾花数据集
iris = load_iris()
X = iris.data  # 特征数据
y = iris.target  # 目标标签

# 使用train_test_split方法切分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建KNN分类器
knn = KNeighborsClassifier(n_neighbors=3)  # 选择K值，这里选择K=3

# 在训练集上训练KNN模型
knn.fit(X_train, y_train)

# 在训练集上进行预测
y_train_pred = knn.predict(X_train)
train_accuracy = accuracy_score(y_train, y_train_pred)

# 在测试集上进行预测
y_test_pred = knn.predict(X_test)
test_accuracy = accuracy_score(y_test, y_test_pred)

# 打印训练集和测试集的准确度
print("训练集准确度: {:.2f}%".format(train_accuracy * 100))
print("测试集准确度: {:.2f}%".format(test_accuracy * 100))
