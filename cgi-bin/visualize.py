import pylab as pl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
data = np.genfromtxt("WEIGHTSAM.csv", delimiter=",")
X = data.data[:, :2]  # we only take the first two features.
Y = data.target
x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
pl.figure(2, figsize=(8, 6))
pl.clf()

# Plot the training points
pl.scatter(X[:, 0], X[:, 1], c=Y, cmap=pl.cm.Paired)
pl.xlabel('x range')
pl.ylabel('y range')

pl.xlim(x_min, x_max)
pl.ylim(y_min, y_max)
pl.xticks(())
pl.yticks(())
