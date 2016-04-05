#!c:\Python27\python.exe
#!/usr/bin/env python
import cgi, cgitb
import numpy as np
import pylab as pl
from sklearn import datasets, svm

iris = datasets.load_weight()
X = iris.data[:, :2]
y = iris.target

#X = X[y != 0, :2]
#y = y[y != 0]

n_sample = len(X)

np.random.seed(0)
order = np.random.permutation(n_sample)
X = X[order]
y = y[order].astype(np.float)

X_train = X[:n_sample]
y_train = y[:n_sample]
X_test = X[n_sample:]
y_test = y[n_sample:]

# fit the model

clf = svm.SVC(kernel='linear')
clf.fit(X_train, y_train)
xx=np.linspace(-1,1,20)
yy=np.linspace(0,1,20)
X1, X2 = np.meshgrid(xx,yy)
Z = np.empty(X1.shape)
for (i, j), val in np.ndenumerate(X1):
    x1 = val
    x2 = X2[i, j]
    p = clf.decision_function(np.c_[x1.ravel(),x2.ravel()])
    Z[i, j] = p[0]
levels = [-1.0, 0.0, 1.0]
linestyles = ['dashed', 'solid', 'dashed']
#colors = 'k'
Z=Z.reshape(X1.shape)
pl.contourf(X1, X2, Z, levels,linestyles=linestyles,cmap=pl.cm.Paired)
pl.scatter(X[:, 0], X[:, 1], c=y, cmap=pl.cm.Paired)

pl.axis('tight')
pl.show()
