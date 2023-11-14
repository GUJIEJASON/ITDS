from sklearn.feature_extraction.text import CountVectorizer

# 例子文本
text = ["This is an example of bag of words model.",
        "You can use it to vectorize any text data for further analysis.",
        "The bag of words model ignores the order of words and only considers their frequency."]

# 创建词袋模型
vectorizer = CountVectorizer()

# 将文本转换为词袋向量
vectorized_text = vectorizer.fit_transform(text)

# 输出结果向量
print("词袋模型的向量化结果：")
print(vectorized_text.toarray())
