# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 20:41:49 2020

@author: Jaspreetsingh_Tuli
"""
import math

#logistic function
def logistic(x):
    ex = math.exp(x)
    return ex/(ex + 1)

#derivative of the logistic function
def logistic_prime(x):
    return logistic(x) * (1 - logistic(x))