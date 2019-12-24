# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from collections import Counter
import math

runs_scored = [219,203, 200, 183,175, 170,166, 166, 158, 158, 154, 149,141,140,140, 140, 140, 140, 125,121,121,119,119,118,118,116,115,115,115,115,114,114,113,113,113,113,112,112,111,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,98, 98, 97, 92, 92, 92, 92, 90,89,89,88,88,87,87,87,87,87,87,80,80,80,79,79,79,79,79,79,71,71,71,70,70,70,70,70,70,65,65,65,63,63,62,62,62,62,62,62,62,62,62,62,62,62,61,61,61,60,60,58,58,58,58,58,58,58,58,58,58,58,58,58,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,54,53,51,51,51,51,51,51,51,51,50,50,50,50,50,50,50,50,50,50,50,50,50,50,49,49,49,49,49,48,48,48,48,47,47,47,47,47,47,47,47,43,43,43,43,40,40,40,37,37,37,37,37,37,37,37,37,37,37,33,33,33,33,33,33,33,33,33,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,29,28,28,28,24,24,24,24,24,23,23,23,23,23,23,23,23,19,19,19,13,13,13,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10, 7,7,7,7,7,7,7,4,4,4,4,4,4,4,4,4,3,2,0,0,0,0,0,0,0,0,0,0]
runs_counts = Counter(runs_scored)
xs = range(251)
ys = [runs_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0,251,0, 35])
plt.title("Histogram")
plt.xlabel("# of runs")
plt.ylabel("# of innings")
plt.show()

num_innings = len(runs_scored)
print("Number of innings played: ", num_innings)
dismissals = 268
largest_value = max(runs_scored)
smallest_value = min(runs_scored)

sorted_values = sorted(runs_scored)
smallest_value = sorted_values[0]
largest_value = sorted_values[-1]

print ("Highest Score: ",largest_value)
print("Lowest Score: ", smallest_value)

def average(x):
    return sum(x)/dismissals

print("Average runs scored per innings: ", average(runs_scored))

def mean(x):
    return sum(x)/len(x)

print("Mean runs scored: ", mean(runs_scored))


#Median of the data
def median(v):
    n= len(v)
    sorted_v = sorted(v)
    midpoint = n//2
    
    if(n%2==1):
        return sorted_v[midpoint]
    else:
        lo = midpoint - 1;
        hi = midpoint
        return ((sorted_v[lo]+sorted_v[hi])/2)
    
print("Median of the given data is: ", median(runs_scored))

#Quantile is the generalization of the median

def quantile(x,p):
    p_index = int(p*len(x))
    return sorted(x)[p_index]


print(quantile(runs_scored, 0.5))


def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items()
            if count == max_count]



print("Runs scored most number of times: ", mode(runs_scored))