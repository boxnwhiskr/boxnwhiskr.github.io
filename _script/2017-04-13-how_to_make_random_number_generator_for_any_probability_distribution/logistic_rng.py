# python3
import math
import random
import numpy as np
from scipy.stats import logistic

from matplotlib import pyplot as plt


def inv_logistic_cdf(u):
    return math.log(u / (1 - u))

random.seed(1001)

# random samples from Unif(0, 1)
random_numbers = [random.random() for _ in range(12000)]

# random samples of Logistic Dist. through the inverse transform
random_numbers_from_logistic = [inv_logistic_cdf(random_number)
                                for random_number in random_numbers]

x = np.linspace(logistic.ppf(0.001), logistic.ppf(0.999), 100)

plt.hist(random_numbers_from_logistic, 60, facecolor='green', normed=True,
         alpha=0.6, label='random numbers')
plt.plot(x, logistic.pdf(x), lw=2, alpha=0.7, label='logistic pdf')
plt.legend(loc='best')

