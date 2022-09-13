# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 13:32:22 2022

@author: trist
"""
import numpy as np
from scipy import stats
from scipy.special import gammaln
import matplotlib.pyplot as plt
from math import comb, log

np.random.seed(0)

# Hyperparameter array, indexed by the scenario.
HYPERS = np.array(
    [[ 1,  1],
     [50, 50],
     [ 5,  1]]
)

SCENARIO = 2
alpha, beta = HYPERS[SCENARIO]

N = 100

n_heads = np.sum(np.random.uniform(0, 1, size=N) < 0.7)
n_tails = N - n_heads

alpha_posterior = alpha + n_heads
beta_posterior = beta + n_tails

x = np.arange(0, 1.01, 0.01)

fig = plt.figure()
ax = fig.gca()
rv_prior = stats.beta(alpha, beta)
ax.plot(x, rv_prior.pdf(x), c="r", label="Prior")
rv_posterior = stats.beta(alpha_posterior, beta_posterior)
ax.plot(x, rv_posterior.pdf(x), c="b", label="Posterior")
ax.legend()
fig.show()


marginal_likelihood = log(comb(N, n_heads))
marginal_likelihood += gammaln(alpha_posterior + beta_posterior)
marginal_likelihood -= gammaln(alpha) + gammaln(beta)
marginal_likelihood += gammaln(alpha_posterior) + gammaln(beta_posterior)
marginal_likelihood -= gammaln(alpha_posterior * beta_posterior + N)
marginal_likelihood = np.exp(marginal_likelihood)

