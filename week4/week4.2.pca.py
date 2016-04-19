__author__ = 'yury'

from sklearn import decomposition
import numpy as np
import pandas as pd

cp = pd.read_csv("data/close_prices.csv")
dj = pd.read_csv("data/djia_index.csv")

cp_data = cp.iloc[:,1:]
dj_data = dj.iloc[:,1]

clf = decomposition.PCA(n_components=10)
components = clf.fit_transform(cp_data)

print(clf.explained_variance_ratio_)

r = 0
for k, v in enumerate(clf.explained_variance_ratio_):
    r+=v
    if r > 0.9:
        print(k+1)
        break

corr = np.corrcoef(components[:, 0], dj_data)
print(round(corr[0][1], 2))
ans = cp_data.columns.values[np.argsort(clf.components_[0])][::-1][0]
print(ans)