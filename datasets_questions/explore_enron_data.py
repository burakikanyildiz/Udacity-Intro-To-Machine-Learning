#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

most=max(enron_data['LAY KENNETH L']['total_payments'],enron_data['SKILLING JEFFREY K']['total_payments'],enron_data['FASTOW ANDREW S']['total_payments'])
print most
item= next(item for item in enron_data.values() if item['total_payments']==most)
print enron_data.keys()[enron_data.values().index(item)]

print len(filter(lambda x: x['salary']!='NaN',enron_data.values()))
print len(filter(lambda x: x['email_address']!='NaN',enron_data.values()))

print len(filter(lambda x: x['total_payments']=='NaN',enron_data.values()))
print float(len(filter(lambda x: x['poi']==True,enron_data.values())))
print float(len(filter(lambda x: x['poi']==True and x['total_payments']=='NaN',enron_data.values())))/len(filter(lambda x: x['poi']==True,enron_data.values()))
print len(enron_data.keys())
