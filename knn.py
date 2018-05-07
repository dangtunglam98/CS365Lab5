from knn_util import *
import sys

def main(filename, k, split, seed):
	
	confuse_accurate = confusion_matrix(filename, k, split, seed)
	accuracy = confuse_accurate[1] * 100
	print("		CONFUSION MATRIX")
	print(confuse_accurate[0])
	print("The accuracy score is " + str(accuracy) + "%")

if __name__ == '__main__':
	filename, k, split, seed = sys.argv[1:]
	main(filename, int(k), float(split), int(seed))
