import os
from sklearn.datasets import load_iris
from sklearn import tree
clf = tree.DecisionTreeClassifier()
iris = load_iris()
clf = clf.fit(iris.data, iris.target)
export_file = tree.export_graphviz(clf,
...     out_file='omtree.dot')
