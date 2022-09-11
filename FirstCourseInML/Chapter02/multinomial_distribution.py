"""
The binomial distribution is an extension of the Bernoulli distribution to 
account for multiple instances
"""
import numpy as np
import matplotlib.pyplot as plt
import math

def multinomial(x, q, N):
    """
    extends the idea of a binomial to vectors
    """

    numerator = math.factorial(N)
    denominator = math.prod(math.factorial(xi) for xi in x)
    probability_product = math.prod(qi ** xi for qi, xi in zip(q, x))

    return (numerator / denominator) * probability_product



def main():
    a, b, c = 1, 2, 3
    players = np.array([a, b, c])
    q1, q2, q3 =  0.2, 0.3, 0.5
    probabilities = np.array([q1, q2, q3])

    p = multinomial(players, probabilities, 6)
    print(p)


if __name__ == "__main__":
    main()