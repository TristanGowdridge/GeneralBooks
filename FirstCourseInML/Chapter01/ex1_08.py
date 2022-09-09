"""
Using the models for the men’s and wmen’s 100 m, find the Olympic games when it
is predicted for women to run a faster winning time than men. What are the
predicted winning times? Do they seem realistic?
"""

import numpy as np
import matplotlib.pyplot as plt

# Need to use __import__, as I've been an idiot and started a file name with a
# number.
mens = __import__("100m_linear_model")
import ex1_06 as womens

def main():
    # Intersection of the two models, the women become faster than men,
    # according to the models.
    year_change = (mens.w0 - womens.w[0]) / (womens.w[1] - mens.w1)

    print(f"Women will be faster than men after {year_change:.2f}")

    # The times from each model at the intersection point.
    print(mens.model(year_change))
    print(womens.model(year_change))

    # Not realistic. The linear models are bad, and extrapolating outside the
    # range of the data is even worse. Assuming the models were true, in the
    # year 10000 the times will be negative.
    print(f"Womens winning time in 10000: {womens.model(10000)}")

if __name__ == "__main__":
    main()