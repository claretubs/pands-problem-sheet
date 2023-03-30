# Program displays two plots:
# Histogram of a normal distribution of a 1000 values with a mean of 5 and standard diviation of 2
# And a plot of the function h(x) = x^3 in the range [1,10]
# On the one set of axes
# Author: Clare Tubridy
# 28-03-2023

import numpy as np
import matplotlib.pyplot as plt

# Ensures random numbers are the same each time its run
np.random.seed(1)
random_histogram = np.random.normal(5, 2, 1000)
# color='r', label='Normal Distribution'

xpoints = np.array(range(1,10))
h_of_x = xpoints * xpoints * xpoints

plt.title('Random Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

plt.hist(random_histogram, color='r', label='Normal Distribution')
plt.plot(xpoints, h_of_x, color='b', label='H(x) = x^3')
plt.show()