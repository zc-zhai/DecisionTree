# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 22:54:58 2018

@author: Administrator
"""

import numpy as np
import pandas
from sklearn.tree import DecisionTreeClassifier
my_data = pandas.read_csv("D:\HTRU_2.csv", delimiter=",")
my_data["Class"] = my_data["Class"].astype("str")
my_data
featureNames = list(my_data.columns.values)[0:8]
featureNames
X = my_data.drop(my_data.columns[[8]], axis=1).values
X[0:5]
targetNames = my_data["Class"].unique().tolist()
targetNames
y = my_data["Class"]
y[0:5]
from sklearn.cross_validation import train_test_split
X_trainset, X_testset, y_trainset, y_testset = train_test_split(X, y, test_size=0.3, random_state=3)
print (X_trainset.shape) 
print (y_trainset.shape)
print (X_testset.shape) 
print (y_testset.shape)
myTree = DecisionTreeClassifier(criterion="entropy")
myTree.fit(X_trainset,y_trainset)
predTree = myTree.predict(X_testset)
print(predTree [0:5])
print(y_testset [0:5])
from sklearn import metrics
import matplotlib.pyplot as plt
print("DecisionTrees's Accuracy: "), metrics.accuracy_score(y_testset, predTree)
from sklearn.externals.six import StringIO
import pydotplus
import matplotlib.image as mpimg
from sklearn import tree
'''%matplotlib inline'''
dot_data = StringIO()
filename = "mytree.png"
out=tree.export_graphviz(myTree,feature_names=featureNames, out_file=dot_data, class_names= np.unique(y_trainset), filled=True,  special_characters=True,rotate=False)  
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png(filename)
img = mpimg.imread(filename)
plt.figure(figsize=(100, 200))
plt.imshow(img,interpolation='nearest')