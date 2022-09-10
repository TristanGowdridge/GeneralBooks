"""
The binomial distribution is an extension of the Bernoulli distribution to 
account for multiple instances
"""
import numpy as np
import matplotlib.pyplot as plt
import math

binomial = lambda x, q, n: math.comb(n, x) * (q ** x) * (1 - q) ** (n - x)

def main():
    REPETITIONS = 50
    PROBABILITY = 0.7

    REPETITIONS += 1
    
    x = np.arange(REPETITIONS)
    y = np.zeros(shape=REPETITIONS)
    for i in x:
        y[i] = binomial(i, PROBABILITY, REPETITIONS)
    
    fig = plt.figure()
    ax = fig.gca()
    ax.bar(x, y)
    ax.set_xlabel("$x$")
    ax.set_ylabel("$p(x)$")
    plt.show()


if __name__ == "__main__":
    main()