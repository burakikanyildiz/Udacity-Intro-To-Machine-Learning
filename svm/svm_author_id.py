#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
import numpy

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
"""params= [
{'C':[10,100,1000,10000], 'kernel':['rbf']}
]
clf_search=GridSearchCV(SVC(),params)
"""


features_train=features_train[:len(features_train)]
labels_train=labels_train[:len(labels_train)]
clf=SVC(kernel='rbf',C=10000)
t0=time()
clf.fit(features_train,labels_train)
print "training time:", round(time()-t0,3),"s"
pred=clf.predict(features_test)
t1=time()
from sklearn.metrics import accuracy_score
print "predicitng time:", round(time()-t1,3),"s"
print accuracy_score(labels_test,pred)
print classification_report(labels_test, pred)
print pred[10]," ", pred[26], " ", pred[50]
unique, counts = numpy.unique(pred, return_counts=True)
print dict(zip(unique, counts))


#########################################################


