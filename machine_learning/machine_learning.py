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
