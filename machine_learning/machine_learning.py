# -*- coding: utf-8 -*-
import random
#Solving the overfitting and underfiiting problem

#Splitting data
def split_data(data, prob):
    """split data into fractions[prob, 1-prob]"""
    #creates a tuple of 2 lists
    results = [],[]
    for row in data:
        results[0 if random.random()<prob else 1].append(row)
    return results



def train_test_split(x, y, test_pct):
    #mapping corresponding values of the matrix x and a vector y
    data = list(zip(x, y))
    #split the dataset of pairs
    train, test = split_data(data, 1 - test_pct)
    #unzipping
    x_train, y_train = list(zip(*train))
    x_test, y_test = list(zip(*test))
    return x_train, x_test, y_train, y_test

#Correctness

def accuracy(true_positive, false_positive, false_negative, true_negative):
    return (true_positive + true_negative)/(true_positive + false_positive + false_negative +true_negative)

#precision measures the accuracy of positive predictions
def precision(tp,fp,fn,tn):
    return tp/(tp+fp)
#recall measures fractions of postives
def recall(tp,fp,fn, tn):
    return tp / (tp+fn)

#f1 score is the harmonic mean of recall and precision
def f1_score(tp, fp, fn, tn):
    p = precision(tp, fp, fn, tn)
    r = recall(tp, fp, fn, tn)
    return 2 * p * r / (p + r)


print("accuracy(70, 4930, 13930, 981070)", accuracy(70, 4930, 13930, 981070))
print("precision(70, 4930, 13930, 981070)", precision(70, 4930, 13930, 981070))
print("recall(70, 4930, 13930, 981070)", recall(70, 4930, 13930, 981070))
print("f1_score(70, 4930, 13930, 981070)", f1_score(70, 4930, 13930, 981070))


