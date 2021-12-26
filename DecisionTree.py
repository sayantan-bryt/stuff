import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report


# Function importing Dataset
def importdata():
    balance_data = pd.read_csv(
        'https://archive.ics.uci.edu/ml/machine-learning-' +
        'databases/balance-scale/balance-scale.data',
        sep=',', header=None)

    # Printing the dataset shape
    # print("Dataset Length: ", len(balance_data))
    # print("Dataset Shape: ", balance_data.shape)
    #
    # # Printing the dataset observations
    # print("Dataset: ", balance_data.head())
    return balance_data


# Function to split the dataset
def splitdataset(balance_data):
    # Separating the target variable
    x = balance_data.values[:, 1:5]
    y = balance_data.values[:, 0]

    # Spliting the dataset into train and test
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.3, random_state=100)

    return x, y, x_train, x_test, y_train, y_test


# Function to perform training with giniIndex.
def train_using_gini(x_train, x_test, y_train):
    # Creating the classifier object
    clf_gini = DecisionTreeClassifier(criterion="gini",
                                      random_state=100, max_depth=3, min_samples_leaf=5)

    # Performing training
    clf_gini.fit(x_train, y_train)
    return clf_gini


# Function to perform training with entropy.
def train_using_entropy(x_train, x_test, y_train):
    # Decision tree with entropy
    clf_entropy = DecisionTreeClassifier(
        criterion="entropy", random_state=100,
        max_depth=3, min_samples_leaf=5)

    # Performing training
    clf_entropy.fit(x_train, y_train)
    return clf_entropy


# Function to make predictions
def prediction(x_test, clf_object):
    # Predicton on test with giniIndex
    y_pred = clf_object.predict(x_test)
    print("Predicted values:")
    print(y_pred)
    return y_pred


# Function to calculate accuracy
def cal_accuracy(y_test, y_pred):
    print("Confusion Matrix: ",
          confusion_matrix(y_test, y_pred))

    print("Accuracy : ",
          accuracy_score(y_test, y_pred) * 100)

    print("Report : ",
          classification_report(y_test, y_pred))


# Driver code
def main():
    # Building Phase
    data = importdata()
    x, y, x_train, x_test, y_train, y_test = splitdataset(data)
    clf_gini = train_using_gini(x_train, x_test, y_train)
    clf_entropy = train_using_entropy(x_train, x_test, y_train)

    # Operational Phase
    print("Results Using Gini Index:")

    # Prediction using gini
    y_pred_gini = prediction(x_test, clf_gini)
    cal_accuracy(y_test, y_pred_gini)

    print("Results Using Entropy:")
    # Prediction using entropy
    y_pred_entropy = prediction(x_test, clf_entropy)
    cal_accuracy(y_test, y_pred_entropy)


# Calling main function
if __name__ == "__main__":
    main()
