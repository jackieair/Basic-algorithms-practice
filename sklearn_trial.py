from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

import pandas as pd
import numpy as np

#读取数据
data = pd.read_csv('data1.csv')

X = np.array(data[['x1','x2']])
y = np.array(data['y'])

"""设置分类器参数"""
classifier = SVC(kernel= 'poly', degree = 2)

"""将数据分成训练和测试集"""
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
print(classifier.fit(X,y))

"""预测结果"""
print(classifier.predict([[0.137777,0.164333]]))
