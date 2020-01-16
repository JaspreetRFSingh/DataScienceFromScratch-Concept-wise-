# -*- coding: utf-8 -*-
import math
import maths_concepts.basic_statistics_operations as bso
import maths_concepts.vector_operations as vo


def data_range(x):
    return max(x) - min(x)

def de_mean(x):
    """translate x by subtracting its mean (so the result has mean 0)"""
    x_bar = bso.mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):
    """assumes x has at least two elements"""
    n = len(x)
    deviations = de_mean(x)
    return vo.sum_of_squares(deviations) / (n - 1)

def standard_deviation(x):
    return math.sqrt(variance(x))

def interquartile_range(x):
    return bso.quantile(x, 0.75) - bso.quantile(x, 0.25)


# CORRELATION




def strike_rate(runs, balls):
    return runs*100/balls



def covariance(x, y):
    n = len(x)
    return vo.dot(de_mean(x), de_mean(y)) / (n - 1)

def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0 # if no variation, correlation is zero



if __name__ == "__main__":
    
    balls_per_innings = [140 ,133, 152, 143,135, 120,126, 101, 150, 121, 123, 101,101,100,131, 130, 128, 137, 125,121,111,99,121,126,125,117,115,125,105,105,94,119,121,100,73,81,129,120,130,130,120,120,121,100,101,106,105,109,102,108,100,70,81,91,101,103,106,107,108,108,90,90,90,97,95,98,99,91,91,92,92,93, 96, 95, 92, 92, 92, 92, 99,109,110,87,68,67,67,52,59,57,97,100,94,90,99,91,90,49,39,89,61,51,67,77,77,79,79,87,87,85,85,68,68,69,73,79,66,69,29,61,60,62,62,62,62,62,61,71,91,40,50,68,61,67,68,60,63,48,43,50,50,60,58,58,54,55,55,55,55,55,55,57,59,55,55,59,65,75,71,55,55,55,73,55,55,66,55,69,55,59,55,54,53,51,51,57,57,59,59,60,31,39,29,21,58,56,55,52,59,54,47,63,67,71,55,59,69,51,49,49,48,48,48,48,49,51,67,49,48,44,49,53,53,53,63,51,50,30,39,37,37,37,37,37,37,37,37,37,37,37,33,33,33,33,33,39,33,33,36,30,35,35,30,30,34,42,43,30,30,30,54,30,30,30,31,33,30,29,26,28,26,24,29,32,34,49,21,20,17,25,29,27,26,21,18,16,13,12,19,19,21,10,5,10,11,13,14,15,11,10,16,9,10,10,10,10, 7,7,5,7,4,9,10,11,14,14,13,10,9,7,4,4,7,9,1,1,10,10,11,4,5,7,1,1]
    total_balls_faced = sum(balls_per_innings)
    total_runs_scored = sum(bso.runs_scored)
    
    print("Total balls faced: ", total_balls_faced)
    print("Total runs: ", total_runs_scored)
    
    print("Career Strike rate: ", strike_rate(total_runs_scored, total_balls_faced))
    
    outlier = bso.runs_scored.index(219) # index of outlier
    
    num_friends_good = [x
                        for i, x in enumerate(bso.runs_scored)
                        if i != outlier]
    
    daily_minutes_good = [x
                          for i, x in enumerate(balls_per_innings)
                          if i != outlier]
    
    #Covariance measures how two variables vary in tandems from their means
    print("Covariation: ",covariance(bso.runs_scored, balls_per_innings))
    
    print("Correlation: ",correlation(bso.runs_scored, balls_per_innings))