import numpy as np
from sklearn.metrics import roc_auc_score
from scipy.spatial import distance
import math

def gd(X, y, k=0.1, w0=None, C=0, eps=1e-5, iteration_limit=10000):
    # if w0 is zero, fill it with zeroes
    if w0 == None:
        w0 = np.array([0.0,0.0])
    w = np.array(w0)[:] #copy w0

    for i in range(0, iteration_limit):
        new_w = gradient_step(X,y,w,k,C)
        diff = distance.euclidean(w, new_w)
        w = new_w
        if diff < eps:
            print("break on iteration ", i)
            break

    return w

def gradient_step(X,y,w,k=0.1,C=0):
    # fill answer with zeroes [0,0]
    out = np.array([0.0,0.0])
    l = len(y)
    # iterate through X,y
    for idx in range(0, l):
        x_cur = X[idx]
        y_cur = y[idx]
        w1 = y_cur * x_cur[0] * (1.0 - 1.0 / (1 + math.exp(-y_cur * np.dot(x_cur, w))))
        w2 = y_cur * x_cur[1] * (1.0 - 1.0 / (1 + math.exp(-y_cur * np.dot(x_cur, w))))
        out[0] += w1
        out[1] += w2

    out *= k / l
    out += w - k * C * w
    return out

def proba(X, w):
    l = len(X)
    p = np.zeros(l)
    for idx in range(0, l):
        x = X[idx]
        p[idx] = (1.0 / (1 + math.exp(-1 * np.dot(x, w))))
    return p

data = np.genfromtxt('data/data-logistic.csv', delimiter=",")

y = data[:,0]
X = data[:,1:]

w = gd(X,y)
w_L2 = gd(X,y,C=10)

p = proba(X, w)
p_L2 = proba(X, w_L2)

roc = roc_auc_score(y, p)
roc_L2 = roc_auc_score(y, p_L2)

res = str(round(roc, 3)) + " " + str(round(roc_L2, 3))
print(res)
