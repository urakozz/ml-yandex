import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn import metrics
from sklearn import datasets
from sklearn import neighbors
from sklearn import cross_validation
from sklearn import preprocessing

data = np.genfromtxt('wine.data', delimiter=",")

y = data[:, 0]
X = data[:, 1:]

kf = cross_validation.KFold(len(data), n_folds=5, random_state=42, shuffle=True)

scores_np = np.empty(51, dtype=[('id', int),('data', float)])
for k in range(1, 51):
    clf = neighbors.KNeighborsClassifier(n_neighbors=k)
    scores = cross_validation.cross_val_score(clf, X, y, scoring='accuracy', cv=kf)
    scores_np[k] = (k, scores.mean())

print(np.sort(scores_np, order='data')[-5:])


X = preprocessing.scale(X)
scores_scaled_np = np.empty(51, dtype=[('id', int),('data', float)])
for k in range(1, 51):
    clf = neighbors.KNeighborsClassifier(n_neighbors=k)
    scores = cross_validation.cross_val_score(clf, X, y, scoring='accuracy', cv=kf)
    scores_scaled_np[k] = (k, scores.mean())
print(np.sort(scores_scaled_np, order='data')[-5:])