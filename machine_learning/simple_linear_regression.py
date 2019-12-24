# -*- coding: utf-8 -*-
from collections import Counter, defaultdict
from maths_concepts.vector_operations import vector_subtract
from maths_concepts.basic_statistics_operations import mean
from maths_concepts.dispersion_and_correlation import correlation, de_mean, standard_deviation
from maths_concepts.gradient_descent import minimize_stochastic
import random
from matplotlib import pyplot as plt
import numpy as np

#line's equation(y=mx+c)
def predict(alpha, beta, x_i):
    return beta * x_i + alpha

#displacement in y (y'-y)
def error(alpha, beta, x_i, y_i):
    return y_i - predict(alpha, beta, x_i)


def sum_of_squared_errors(alpha, beta, x, y):
    return sum(error(alpha, beta, x_i, y_i) ** 2
               for x_i, y_i in zip(x, y))

def least_squares_fit(x,y):
    beta = correlation(x, y) * standard_deviation(y) / standard_deviation(x)
    alpha = mean(y) - beta * mean(x)
    return alpha, beta

def total_sum_of_squares(y):
    return sum(v ** 2 for v in de_mean(y))

def r_squared(alpha, beta, x, y):

    return 1.0 - (sum_of_squared_errors(alpha, beta, x, y) /
                  total_sum_of_squares(y))

def squared_error(x_i, y_i, theta):
    alpha, beta = theta
    return error(alpha, beta, x_i, y_i) ** 2

def squared_error_gradient(x_i, y_i, theta):
    alpha, beta = theta
    return [-2 * error(alpha, beta, x_i, y_i),       
            -2 * error(alpha, beta, x_i, y_i) * x_i] 

if __name__ == "__main__":

    #x (independent variable)
    num_runs_scored = np.array([49,41,40,25,121,12,109,89,18,0,16,49,21,215,15,14,19,103,130,139,153,152,162,141,100,110,109,140,10,0,0,14,67,75,86,50,59,22,43])
    #y (dependent variable)
    num_balls_faced = np.array([68,51,52,38,144,17,151,41,31,1,14,38,47,109,27,41,36,48,128,146,135,132,135,126,123,89,40,91,31,0,8,21,26,27,23,46,30,33,24])


    alpha, beta = least_squares_fit(num_runs_scored, num_balls_faced)
    print("alpha", alpha)
    print("beta", beta)

    print("r-squared", r_squared(alpha, beta, num_runs_scored, num_balls_faced))
    
    y_predict = alpha + beta*num_runs_scored
    print(y_predict)
    plt.title("y="+str(beta)+"x+"+str(alpha))
    plt.plot(num_runs_scored, num_balls_faced, 'o')
    plt.xlabel("Number of runs")
    plt.ylabel("Number of balls")
    plt.plot(num_runs_scored, y_predict, 'k-', color='red')
    
    print()

    print("gradient descent:")
    random.seed(0)
    theta = [random.random(), random.random()]
    alpha, beta = minimize_stochastic(squared_error,
                                      squared_error_gradient,
                                      num_runs_scored,
                                      num_balls_faced,
                                      theta,
                                      0.0001)
    print("alpha", alpha)
    print("beta", beta)
    y_predict = alpha + beta*num_runs_scored
    print(y_predict)
    plt.title("y="+str(beta)+"x+"+str(alpha))
    plt.plot(num_runs_scored, num_balls_faced, 'o')
    plt.xlabel("Number of runs")
    plt.ylabel("Number of balls")
    plt.plot(num_runs_scored, y_predict, 'k-', color='blue')
    
