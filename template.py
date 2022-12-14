#PLEASE WRITE THE GITHUB URL BELOW!
#https://github.com/SeoyoungKK/oss_assignment2.git

import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score

def load_dataset(dataset_path):
	#To-Do: Implement this function
        df = pd.read_csv(dataset_path)
        return df
def dataset_stat(dataset_df):	
	#To-Do: Implement this function
        n_feats = len(dataset_df.drop('target', axis=1).columns)
        n_class0 = dataset_df.groupby("target").size()[0]
        n_class1 = dataset_df.groupby("target").size()[1]
        return n_feats, n_class0, n_class1

def split_dataset(dataset_df, testset_size):
	#To-Do: Implement this function
        X_train, X_test, y_train, y_test = train_test_split(dataset_df.drop('target', axis=1), dataset_df['target'], test_size=testset_size)
        return X_train, X_test, y_train, y_test

def decision_tree_train_test(x_train, x_test, y_train, y_test):
	#To-Do: Implement this function
        dt_clf = DecisionTreeClassifier()
        dt_clf.fit(x_train, y_train)
        prediction = dt_clf.predict(x_test)
        acc = accuracy_score(y_test, prediction)
        prec = precision_score(y_test, prediction)
        recall = recall_score(y_test, prediction)
        return acc, prec, recall

def random_forest_train_test(x_train, x_test, y_train, y_test):
	#To-Do: Implement this function
        rf_clf = RandomForestClassifier()
        rf_clf.fit(x_train, y_train)
        prediction = rf_clf.predict(x_test)
        acc = accuracy_score(y_test, prediction)
        prec = precision_score(y_test, prediction)
        recall = recall_score(y_test, prediction)
        return acc, prec, recall

def svm_train_test(x_train, x_test, y_train, y_test):
	#To-Do: Implement this function
        svm_clf = SVC()
        svm_clf.fit(x_train, y_train)
        prediction = svm_clf.predict(x_test)
        acc = accuracy_score(y_test, prediction)
        prec = precision_score(y_test, prediction)
        recall = recall_score(y_test, prediction)
        return acc, prec, recall

def print_performances(acc, prec, recall):
	#Do not modify this function!
	print ("Accuracy: ", acc)
	print ("Precision: ", prec)
	print ("Recall: ", recall)

if __name__ == '__main__':
	#Do not modify the main script!
	data_path = sys.argv[1]
	data_df = load_dataset(data_path)

	n_feats, n_class0, n_class1 = dataset_stat(data_df)
	print ("Number of features: ", n_feats)
	print ("Number of class 0 data entries: ", n_class0)
	print ("Number of class 1 data entries: ", n_class1)

	print ("\nSplitting the dataset with the test size of ", float(sys.argv[2]))
	x_train, x_test, y_train, y_test = split_dataset(data_df, float(sys.argv[2]))

	acc, prec, recall = decision_tree_train_test(x_train, x_test, y_train, y_test)
	print ("\nDecision Tree Performances")
	print_performances(acc, prec, recall)

	acc, prec, recall = random_forest_train_test(x_train, x_test, y_train, y_test)
	print ("\nRandom Forest Performances")
	print_performances(acc, prec, recall)

	acc, prec, recall = svm_train_test(x_train, x_test, y_train, y_test)
	print ("\nSVM Performances")
	print_performances(acc, prec, recall)
