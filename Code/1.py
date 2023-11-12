import numpy as np
from sklearn.linear_model import LinearRegression

x=np.linspace(0,30,30)
y=9*x+8+np.random.randn(30)
model = LinearRegression()
model.fit(x.reshape(-1,1), y.reshape(-1,1))
y_pred = model.predict(x.reshape(-1,1))
print(y_pred)
print(y_pred - y.reshape(-1,1))
r_sq = model.score(x.reshape(-1,1), y.reshape(-1,1))
print('coefficient of determination:', r_sq)
