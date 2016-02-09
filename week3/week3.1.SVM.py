import numpy as np
import pandas as pd
from sklearn import svm

data = np.genfromtxt('data/svm-data.csv', delimiter=",")
X = data[:,1:]
y = data[:,0]

clf = svm.SVC(C=100000, kernel='linear', random_state=241)
clf.fit(X, y)

print(clf.support_ + 1)