import numpy as np
from sklearn import datasets
from sklearn import svm
from sklearn import feature_extraction
from sklearn import grid_search

newsgroups = datasets.fetch_20newsgroups(
    subset='all',
    categories=['alt.atheism', 'sci.space']
)

vectorizer = feature_extraction.text.TfidfVectorizer()

y = newsgroups.target
X_train = vectorizer.fit_transform(newsgroups.data)

parameters = {'C':[1, 10]}

svr = svm.SVC(kernel='linear', random_state=241)
clf = grid_search.GridSearchCV(svr, parameters, cv=5)
clf.fit(X_train, y)

weights = clf.best_estimator_.coef_.toarray()[0]
print(clf.best_estimator_.coef_.todense())
f = np.vectorize(abs)
weights_abs = f(weights)
top10i = np.argsort(weights_abs)[-10:]

feature_names = vectorizer.get_feature_names()
feature_names = np.array(feature_names)

print("Most weighted words:")
print(feature_names[top10i][::-1])

res = np.sort(feature_names[top10i])
print("Answer:")
print(" ".join(res))