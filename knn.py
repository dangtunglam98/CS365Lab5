import random
import math
import csv
import operator
def load_data(filename, seed, split):
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
	
def euclidian_distance(point1, point2):
	distance = 0
	for element in range (len(point1)-1):
		distance += (float(point1[element+1]) - float(point2[element+1]))**2
	return math.sqrt(distance)

def findKNN(data_point, trainingSet, k):
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
	KNN_labels = []
	for item in knn:
		KNN_labels.append(item[0])
	return most_common(KNN_labels)

def main(filename, k, split, seed):
	trainingSet, testSet = load_data(filename, seed, split)
	correct = 0
	total = len(testSet)
	for item in testSet:
		knn = findKNN(item, trainingSet, k)
		pred_label = classify(knn)
		if pred_label == item[0]:
			correct += 1
	accuracy = correct/total
	return accuracy

#print(load_data("iris.csv", 12345, 0.75))
print(main("iris.csv", 3, 0.5, 12345))