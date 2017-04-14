from random import uniform

import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm


def trucated_norm_rng(size, mu=0, sigma=1, lower_bound=None, upper_bound=None):
    u_lower = norm.cdf(lower_bound, mu, sigma) if lower_bound is not None else 0
    u_upper = norm.cdf(upper_bound, mu, sigma) if upper_bound is not None else 1
    rns_unif = (uniform(u_lower, u_upper) for _ in range(size))
    return (norm.ppf(rn_unif, mu, sigma) for rn_unif in rns_unif)

rng_truncated_norm = trucated_norm_rng(10000, 2, 3, 1, 5)

rng = list(trucated_norm_rng(10000, 2, 3, 1, 5))

x = np.linspace(norm.ppf(0.0001, 2, 3), norm.ppf(0.9999, 2, 3), 100)

plt.hist(rng, 20, facecolor='green', normed=False,
         alpha=0.6, label='random numbers', weights=np.ones_like(rng) * 0.00024)
plt.plot(x, norm.pdf(x, 2, 3), lw=2, alpha=0.7, label='N(2, 9) pdf')
plt.legend(loc='best')

