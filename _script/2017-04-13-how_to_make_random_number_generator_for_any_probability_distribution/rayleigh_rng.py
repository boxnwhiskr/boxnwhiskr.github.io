# python3
import math
import random
import numpy as np
from scipy.stats import rayleigh

from matplotlib import pyplot as plt


def inv_rayleigh_cdf(u):
    return math.sqrt(-2 * math.log(1 - u))

random.seed(1001)

# random samples from Unif(0, 1)
random_numbers = [random.random() for _ in range(10000)]

# random samples of Rayleigh Dist. through the inverse transform
random_numbers_from_rayleigh = [inv_rayleigh_cdf(random_number)
                                for random_number in random_numbers]

x = np.linspace(rayleigh.ppf(0), rayleigh.ppf(0.999), 100)

plt.hist(random_numbers_from_rayleigh, 60, facecolor='green', normed=True,
         alpha=0.6, label='random numbers')
plt.plot(x, rayleigh.pdf(x), lw=2, alpha=0.7, label='Rayleigh pdf')
plt.legend(loc='best')

