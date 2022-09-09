"""
Using the data provided in Table 1.3, find the linear model that minimises the
squared loss.
"""

import numpy as np
import matplotlib.pyplot as plt

from ex1_02 import linear_regression_weights

x =(
    1928, 1932, 1936, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980,
    1984, 1988, 1992, 1996, 2000, 2004, 2008
) 

t =(
    12.20, 11.90, 11.50, 11.90, 11.50, 11.50, 11.00, 11.40, 11.00, 11.07,
    11.08, 11.06, 10.97, 10.54, 10.82, 10.94, 11.12, 10.93, 10.78
)

x = np.array(x)
t = np.array(t)

w = linear_regression_weights(x, t)

model = lambda x: w[0] + x * w[1]

def main():
    print(f"The model weights are: {w}")

    fig = plt.figure()
    ax = fig.gca()

    ax.scatter(x, t)
    ax.plot(x, model(x))
    plt.show()

if __name__ == "__main__":
    main()