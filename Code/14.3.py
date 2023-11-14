from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer

# 从20newsgroups数据集中加载数据
newsgroups = fetch_20newsgroups(subset='train')

# 获取文本数据
text_data = newsgroups.data

# 创建TF-IDF向量化器
vectorizer = TfidfVectorizer()

# 将文本转换为TF-IDF向量
tfidf_vector = vectorizer.fit_transform(text_data)

# 输出第一个文本的TF-IDF向量
first_text_tfidf_vector = tfidf_vector[0]

print("第一个文本的TF-IDF向量：")
print(first_text_tfidf_vector.toarray())
