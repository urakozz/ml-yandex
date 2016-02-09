__author__ = 'yury'

import pandas
import numpy as np
from sklearn.tree import DecisionTreeClassifier

data = pandas.read_csv('titanic.csv', index_col='PassengerId')
data["SexF"] = data["Sex"].apply(lambda s: 1 if s == "male" else 0)

filtered = data[data["Age"].notnull()]
X = filtered[["Fare", "Age", "SexF", "Pclass"]]
Y = filtered[["Survived"]]

clf = DecisionTreeClassifier(random_state=241)
clf.fit(np.array(X), np.array(Y))

print("Importances:\n")
print('"Fare", "Age", "SexF", "Pclass"\n')
print(clf.feature_importances_)