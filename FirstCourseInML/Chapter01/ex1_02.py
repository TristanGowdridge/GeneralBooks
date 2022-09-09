"""
Write a python script that will find w0 and w1 for an arbitrary dataset.
"""
import numpy as np
import matplotlib.pyplot as plt

def linear_regression_weights(x, y):
    """
    Returns the weights for a linear regression.
    """
    SAMPLES = len(x)
    x = np.vstack([np.ones(SAMPLES), x]).T
    w = np.dot(np.dot(np.linalg.inv(np.dot(x.T, x)), x.T), y)

    return w

NUMBER_OF_POINTS = 20
x = np.arange(NUMBER_OF_POINTS)
y = x * x
y = y + np.random.normal(loc=0, scale=10, size=NUMBER_OF_POINTS)

w = linear_regression_weights(x, y)
model = lambda x: w[0] + w[1] * x

def main():
    fig = plt.figure()
    ax = fig.gca()

    ax.scatter(x, y)
    ax.plot(x, model(x))
    plt.show()

if __name__ == "__main__":
    main()