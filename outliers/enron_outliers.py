#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop('TOTAL',0)
data_dict_sorted=sorted(data_dict,key=lambda key: data_dict[key]['exercised_stock_options'])
for i in range(len(data_dict_sorted)):
	print data_dict_sorted[i], data_dict[data_dict_sorted[i]]['exercised_stock_options']
print max(data_dict, key=lambda key: data_dict[key]['salary'])
print max(data_dict, key=lambda key: data_dict[key]['salary'])
data = featureFormat(data_dict, features)


### your code below
for point in data:
	salary=point[0]
	bonus=point[1]
	matplotlib.pyplot.scatter(salary,bonus)

matplotlib.pyplot.xlabel('salary')
matplotlib.pyplot.ylabel('bonus')
matplotlib.pyplot.show()


