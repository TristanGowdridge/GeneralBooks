"""
The Bernoulli distribution is a binary random variable. Where the probability
of the event occuring is defiend by q.
"""
import numpy as np
import matplotlib.pyplot as plt

bernoulli = lambda q, x: (q ** x) * (1 - q) ** (1 - x)

def main():
    x = np.arange(2)
    y = bernoulli(0.8, x)
    fig = plt.figure()
    ax = fig.gca()
    ax.scatter(x, y)
    ax.set_xlabel("$x$")
    ax.set_ylabel("$p(x)$")
    plt.show()

if __name__ == "__main__":
    main()