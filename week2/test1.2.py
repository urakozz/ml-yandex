import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn import metrics
from sklearn import datasets
from sklearn import neighbors
from sklearn import cross_validation
from sklearn import preprocessing

data = datasets.load_boston()
X = data.data
y = data.target

X_scaled = preprocessing.scale(X)

kf = cross_validation.KFold(len(y), n_folds=5, random_state=42, shuffle=True)
max_val = None
max_p = 0
for p in np.linspace(1, 10, num=200):
    clf = neighbors.KNeighborsRegressor(n_neighbors=5, weights='distance', p=p)
    scores = cross_validation.cross_val_score(clf, X_scaled, y, cv=kf, scoring='mean_squared_error')
    m = scores.mean()

    if max_val == None or m > max_val:
        max_val = m
        max_p = p

print (max_p, max_val)
