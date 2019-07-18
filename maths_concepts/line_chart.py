# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 123.2, 543.21, 890.90, 239.18, 14958.99, 10289.7]

plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

plt.title("Nominal GDP")

plt.ylabel("Billions of $")

plt.show()

