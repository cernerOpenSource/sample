import numpy as np
import pylab as pl
from sklearn import datasets, svm

iris = datasets.load_iris()
X = iris.data[:, :2]
y = iris.target

X = X
y = y

n_sample = len(X)

np.random.seed(0)
order = np.random.permutation(n_sample)
X = X[order]
y = y[order].astype(np.float)



# fit the model

clf = svm.SVC(kernel='linear', gamma=10)
clf.fit(X ,y)

pl.figure()
pl.clf()
pl.scatter(X[:, 0], X[:, 1], c=y, zorder=10, cmap=pl.cm.Paired)

# Circle out the test data

pl.axis('tight')
x_min = X[:, 0].min()
x_max = X[:, 0].max()
y_min = X[:, 1].min()
y_max = X[:, 1].max()

XX, YY = np.mgrid[x_min:x_max:200j, y_min:y_max:200j]
Z = clf.decision_function(np.c_[XX.ravel(), YY.ravel()])

# Put the result into a color plot
Z = Z.reshape(XX.shape)
pl.pcolormesh(XX, YY, Z > 0, cmap=pl.cm.Paired)
pl.contour(XX, YY, Z, colors=['k', 'k', 'k'], linestyles=['--', '-', '--'],
           levels=[-.5, 0, .5])


pl.show()
