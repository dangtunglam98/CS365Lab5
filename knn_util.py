import random
import math
import csv
import operator
def load_data(filename, seed, split):
	"""Return the training set and test set"""
	csvDataFile = open(filename)
	dataset = csv.reader(csvDataFile)
	dataset = list(dataset)
	csvDataFile.close()
	trainingSet = []
	testSet = []
	label = dataset[0]
	dataset.remove(label)
	countTrain = 0
	countTest = 0
	random.seed(seed)
	random.shuffle(dataset)
	no_split = round(len(dataset)*split)
	trainingSet = dataset[:no_split]
	testSet = dataset[no_split:]

	return trainingSet, testSet
	
def checkFeatureAlpha(string):
	"""Return True if the feature is a string"""
	strFT = False
	for char in string:
		if char.isalpha():
			strFT = True
	return strFT

def euclidian_distance(point1, point2):
	"""Return euclidian distance of 2 datapoints"""
	distance = 0
	for element in range (len(point1)-1):
		if checkFeatureAlpha(point1[element+1]) or checkFeatureAlpha(point2[element+1]):
			if point1[element+1] != point2[element+1]:
				distance += 1
		else:
			distance += (float(point1[element+1]) - float(point2[element+1]))**2
	return math.sqrt(distance)

def findKNN(data_point, trainingSet, k):
	"""Return the k nearest datapoints"""
	neighbors = []
	knn = []
	for item in trainingSet:
		distance = euclidian_distance(data_point,item)
		neighbors.append((item,distance))
	neighbors.sort(key=operator.itemgetter(1))
	for near in range (k):
		knn.append(neighbors[near][0])
	return knn

def most_common(lst):
	 return max(lst, key=lst.count)

def classify(knn):
	"""Return the predicted label"""
	KNN_labels = []
	for item in knn:
		KNN_labels.append(item[0])
	return most_common(KNN_labels)


def get_result_label(dataset):
	labels = []
	for row in dataset:
		if row[0] not in labels:
			labels.append(row[0])
	return labels



def confusion_matrix_util(filename, k, split, seed):
	trainingSet, testSet = load_data(filename, seed, split)
	correct = 0
	total = len(testSet)
	actual = {}
	for actual_label in get_result_label(trainingSet):
		actual[actual_label] = {}
		for prediction in get_result_label(trainingSet):
			actual[actual_label][prediction] = 0
	for item in testSet:
		knn = findKNN(item, trainingSet, k)
		pred_label = classify(knn)
		if pred_label == item[0]:
			correct += 1
		if pred_label not in actual[item[0]]:
			actual[item[0]][pred_label] = 1
		else:
			actual[item[0]][pred_label] += 1
	accuracy = correct/total

	return actual , accuracy
def get_unique(lst):
	unique = []
	for item in lst:
		if item not in unique:
			unique.append(item)
	return unique

def confusion_matrix(filename, k, split, seed):
	"""Return the confusion matrix and accuracy"""
	util = confusion_matrix_util(filename, k, split, seed)
	con_mat = util[0]
	pred_labels = []
	pred_and_actual = []
	for key, val in con_mat.items():
		newEntry = []
		for pred_label, freq in val.items():
			pred_labels.append(pred_label)
			newEntry.append(freq)
		newEntry.append(key)
		pred_and_actual.append(newEntry)
	pred_labels = [get_unique(pred_labels)]
	conf_mat_list = pred_labels + pred_and_actual
	display = ""
	for item in conf_mat_list:
		display = display + "	".join(str(x) for x in item) + "\n"
	accuracy = util[1]
	return display,accuracy




