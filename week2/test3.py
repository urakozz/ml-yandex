import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn import metrics
from sklearn import datasets
from sklearn import preprocessing

data_train = np.genfromtxt('2.train.csv', delimiter=",")
data_test = np.genfromtxt('2.test.csv', delimiter=",")


X_train = data_train[:,1:]
y_train = data_train[:,0]

X_test = data_test[:,1:]
y_test = data_test[:,0]

clf = linear_model.Perceptron(random_state=241)

clf.fit(X_train, y_train)
predictions = clf.predict(X_test)

scaler = preprocessing.StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

clf.fit(X_train_scaled, y_train)
predictions_norm = clf.predict(X_test_scaled)

accuracy = metrics.accuracy_score(y_test, predictions)
accuracy_norm = metrics.accuracy_score(y_test, predictions_norm)
print(accuracy_norm-accuracy)