import numpy as np
import matplotlib.pyplot as plt

SAMPLES = 1000 

y = np.random.normal(0, 2, SAMPLES)
y += np.linspace(0, 30, SAMPLES)
y += 3

x = np.arange(SAMPLES)                  # Linear contribution.
x = np.vstack([np.ones(SAMPLES), x]).T  # Constant and linear contributions.

# Calculate the weights vector.
w = np.dot(np.dot(np.linalg.inv(np.dot(x.T, x)), x.T), y)

linear_approx = lambda x: w[0] + w[1] * x 

plt.plot(y)
plt.plot(linear_approx(x[:, 1]))
plt.show()