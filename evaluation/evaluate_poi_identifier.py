#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list,sort_keys='../tools/python2_lesson14_keys.pkl')
labels, features = targetFeatureSplit(data)



### your code goes here 
### it's all yours from here forward!  
from sklearn.tree import DecisionTreeClassifier
clf=DecisionTreeClassifier()
clf.fit(features,labels)
pred=clf.predict(features)
from sklearn.metrics import accuracy_score
print accuracy_score(pred,labels)

from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(features,labels,random_state=42, test_size=0.3)
print labels_test.count(1) # total number of POI's
print len(labels_test) #total test set
clf2=DecisionTreeClassifier()
clf2.fit(features_train,labels_train)
pred2=clf2.predict(features_test)
temp=[i for i,j in zip(pred2,labels_test) if i==j and i==1] #true positives
print len(temp) #number of true positives
from sklearn.metrics import precision_score,recall_score
print accuracy_score(pred2,labels_test)
print precision_score(pred2,labels_test)
print recall_score(pred2,labels_test)

