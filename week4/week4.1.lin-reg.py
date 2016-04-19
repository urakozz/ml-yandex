__author__ = 'yury'

from sklearn import feature_extraction
from sklearn import linear_model
import numpy as np
import pandas as pd
from scipy.sparse import hstack

data = pd.read_csv("data/salary-train.csv")
data_test = pd.read_csv("data/salary-test-mini.csv")

data["FullDescription"] = data["FullDescription"].str.lower().replace('[^a-z0-9]', ' ', regex = True)
data_test["FullDescription"] = data_test["FullDescription"].str.lower().replace('[^a-z0-9]', ' ', regex = True)

data['LocationNormalized'].fillna('nan', inplace=True)
data['ContractTime'].fillna('nan', inplace=True)
data_test['LocationNormalized'].fillna('nan', inplace=True)
data_test['ContractTime'].fillna('nan', inplace=True)

vector_dict = feature_extraction.DictVectorizer()
X_train_categ = vector_dict.fit_transform(data[['LocationNormalized', 'ContractTime']].to_dict('records'))
X_test_categ = vector_dict.transform(data_test[['LocationNormalized', 'ContractTime']].to_dict('records'))

vector_text = feature_extraction.text.TfidfVectorizer(min_df=5)
X_train_desc = vector_text.fit_transform(data["FullDescription"])
X_test_desc = vector_text.transform(data_test["FullDescription"])

X_train = hstack([X_train_desc, X_train_categ])
X_test = hstack([X_test_desc, X_test_categ])

clf = linear_model.Ridge(alpha=1)
clf.fit(X_train, data["SalaryNormalized"])
predict = clf.predict(X_test)
print(" ".join([str(round(s, 2)) for s in predict]))