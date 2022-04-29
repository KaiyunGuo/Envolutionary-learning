"""
My collection of fitness evaluation methods

Student number:20090444
Student name:Kaiyun Guo
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn import ensemble
from sklearn import svm
import math

def fitness(ind, data):
    #print(data.head)
    y = data.corona_result
    data.drop("corona_result", axis=1, inplace=True)
    # target feature: severity is already chosen
    temp = [i for i in range(len(ind) - 1) if ind[i] != 1]

    data.drop(data.columns[temp], axis=1, inplace=True)

    # fitness = matching_entites(data, ind)
    fit = logistic_model(data, y)
    # print(fitness)
    return fit

def fitness1(ind, data):
    #print(data.head)
    y = data.severity
    data.drop("severity", axis=1,inplace=True)
    # target feature: severity is already chosen
    temp = [i for i in range(len(ind)-1) if ind[i] != 1]

    data.drop(data.columns[temp], axis=1, inplace=True)
    # print(ind, data.columns)
    # print(data.head(10))

    # fitness = matching_entites(data, y)
    fit = logistic_model(data, y)
    # print(fitness)
    return fit

# def matching_entites(data, ind):
#     data = np.array(data)
#     data = data.tolist()
#     fit = []
#     for i in range(len(data)):
#         count = 0
#         for j in range(len(ind)):
#             if ind[j] == data[i][j]:
#                 count += 1
#         fit.append(count)
#     a = sum(fit) // len(fit)
#     return a


def logistic_model(X, y):
    # logistic regression
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=1)
    lr = LogisticRegression(max_iter=1000)
    lr.fit(X_train, y_train)
    y_pr = lr.predict(X_test)
    return accuracy_score(y_test, y_pr) * 100


def comparision(data):
    y = data.corona_result
    data.drop("corona_result", axis=1, inplace=True)
    print(data.columns)
    # print(data.head(10))
    X_train, X_test, y_train, y_test = train_test_split(data, y, test_size=0.1, random_state=1)
    print("Random Forest:")
    rf(X_train, X_test, y_train, y_test)
    print("SVM:")
    SVM(X_train, X_test, y_train, y_test)


def comparision1(data):
    y = data.severity
    data.drop("severity", axis=1, inplace=True)
    print(data.columns)
    # print(data.head(10))
    X_train, X_test, y_train, y_test = train_test_split(data, y, test_size=0.1, random_state=1)
    print("Random Forest:")
    rf(X_train, X_test, y_train, y_test)
    print("SVM:")
    SVM(X_train, X_test, y_train, y_test)


def rf(X_train, X_test, y_train, y_test):
    rf = ensemble.RandomForestClassifier()
    rf.fit(X_train, y_train)
    y_rf = rf.predict(X_test)
    imp = rf.feature_importances_
    print(imp)
    rank = np.argsort(imp)
    print(rank)
    rf_score = accuracy_score(y_test, y_rf)
    print(rf_score)


def SVM(X_train, X_test, y_train, y_test):
    lr = svm.SVC()
    lr.fit(X_train, y_train)
    y_lr = lr.predict(X_test)
    print(accuracy_score(y_test, y_lr))
