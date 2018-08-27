from sklearn.svm import SVC
import numpy as np

X = [[-1, -1], [-2, -1], [1, 1], [2, 1]]
y = [1, 1, 2, 2]

clf = SVC()
clf.fit(X, y)
print (clf.fit(X, y))
print (type(clf.predict([[-0.8, -1]])))
print(type(X))