# -*- coding: utf-8 -*-

from collections import Counter
import math, random
import matplotlib.pyplot as plt
from maths_concepts.probability_distribution import inverse_normal_cdf


#One Dimensional data
def bucketize(point, bucket_size):
    """floor the point to the next lower multiple of bucket_size"""
    return bucket_size * math.floor(point / bucket_size)

def make_histogram(points, bucket_size):
    """buckets the points and counts how many in each bucket"""
    return Counter(bucketize(point, bucket_size) for point in points)

def plot_histogram(points, bucket_size, title=""):
    histogram = make_histogram(points, bucket_size)
    plt.bar(histogram.keys(), histogram.values(), width=bucket_size)
    plt.title(title)
    plt.show()
    
random.seed(0)
uniform = [200*random.random() - 100 for  _ in range(10000)]
normal = [57*inverse_normal_cdf(random.random())
         for _ in range(10000)]

plot_histogram(uniform, 10, "Uniform Histogram")
plot_histogram(normal, 10, "Normal Histogram")



#exploring two dimensional data
def random_normal():
    """returns a random draw from a standard normal distribution"""
    return inverse_normal_cdf(random.random())

xs = [random_normal() for _ in range(1000)]
ys1 = [ x + random_normal() / 2 for x in xs]
ys2 = [-x + random_normal() / 2 for x in xs]


plt.scatter(xs, ys1, marker='.', color='red', label='ys1')
plt.scatter(xs, ys2, marker='.', color='blue',  label='ys2')
plt.xlabel('xs')
plt.ylabel('ys')
plt.legend(loc=9)
plt.show()