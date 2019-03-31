#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):

	cleaned_data = []

	import math
	length=len(predictions)
	lenToRemove=length/10
	print lenToRemove
	diffs=[]
	for i in range(length):
		diff=math.pow(predictions[i]-net_worths[i],2)
		diffs.append({'index':i,'diff':diff})
	diffs=sorted(diffs,key=lambda x : x['diff'],reverse=True)
	print diffs
	for i in range(lenToRemove):
		print ages[diffs[i]['index']], net_worths[diffs[i]['index']]
		del diffs[0]
	print diffs
	diffs=sorted(diffs,key=lambda x:x['index'])
	for i in range(len(diffs)):
		cleaned_data.append(tuple((ages[diffs[i]['index']],net_worths[diffs[i]['index']],diffs[i]['diff'])))
	

	return cleaned_data


# return a list of tuples named cleaned_data where each tuple is of the form (age,net_worth,error)