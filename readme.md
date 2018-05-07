CS365: Artificial Intelligence and Machine Learning
Anh Dang and Lam Dang
Lab E: KNN Classifier

How to run the classifier:
- Open Terminal and cd to the folder contaning the files related to the assignment
- Write command under this format "python knn.py [dataset_file_name] [k_value] [percentage_dataset_as_training_set] [seed]"
- The output would show in the terminal, including the Confusion Matrix and The accuracy of the test set

Note:
- Write filename in the form of string, include .csv. Other than that, all parameter should be written as a numeric value
- The percentage should be 0 < x < 1. Example: if it is 75% you want, write 0.75
- The file mnist_large should take a few minute to run, longer than other small datafile

For report purposes:
1/ Pick a single random seed and a single (sensible) training set percentage and run k-Nearest Neighbor with a k = 1 on each of the four data sets. What is the accuracy you observed on each data set? Include the terminal commands you used to run each of these in your README.

- python knn.py "iris.csv" 1 0.75 12345
- python knn.py "monks1.csv" 1 0.75 12345
- knn.py "mnist_small.csv" 1 0.75 12345
- knn.py "mnist_small.csv" 1 0.75 12345

2/ How did your accuracy compare between the mnist_small and mnist_large data sets? Which had the higher average? 
knn.py "mnist_small.csv" 1 0.5 12345: Accuracy = 94%
knn.py "mnist_small.csv" 1 0.75 12345: Accuracy = 96.8%
knn.py "mnist_small.csv" 1 0.8 12345: Accuracy = 98%
knn.py "mnist_large.csv" 1 0.5 12345: Accuracy = 98.398%
knn.py "mnist_large.csv" 1 0.75 12345: Accuracy = 98.647%
knn.py "mnist_large.csv" 1 0.8 12345: Accuracy = 98.754%

3/ Pick one data set and three different values of k. Run the program with each value of k on that data set and compare the accuracy values observed. Did changing the value of k have much of an effect on your results? Speculate as to why or why not that observation occurred? Include the terminal commands you used to run each of these in your README.

knn.py "mnist_small.csv" 3 0.75 12345
knn.py "mnist_small.csv" 5 0.75 12345
knn.py "mnist_small.csv" 7 0.75 12345

5/ Devise at least one interesting question you wish to know the answer to, distinct from the above, and run experiments to provide evidence to answer it. This might involve using a different distance function, investigating timing issues, or anything else. You will likely need to run additional code for this part of the lab; the code you write here should not interfere with what you’ve written for the earlier parts.

python knn.py "monks1.csv" 4 0.75 12345
python knn.py "mnist_small.csv" 9 0.75 12345