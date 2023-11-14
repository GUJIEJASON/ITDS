from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets import fetch_20newsgroups

# 加载20newsgroups数据集
newsgroups = fetch_20newsgroups(subset='all')

# 获取文本数据和标签
X = newsgroups.data
y = newsgroups.target

# 将数据集划分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建TF-IDF向量化器
vectorizer = TfidfVectorizer()

# 将文本数据转换为TF-IDF向量
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# 创建朴素贝叶斯分类器
classifier = MultinomialNB()

# 在训练集上训练分类器
classifier.fit(X_train_tfidf, y_train)

# 在训练集上进行预测
train_predictions = classifier.predict(X_train_tfidf)

# 在测试集上进行预测
test_predictions = classifier.predict(X_test_tfidf)

# 计算训练集和测试集的准确度
train_accuracy = accuracy_score(y_train, train_predictions)
test_accuracy = accuracy_score(y_test, test_predictions)

print("训练集准确度：", train_accuracy)
print("测试集准确度：", test_accuracy)
