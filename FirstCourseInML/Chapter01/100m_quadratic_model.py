import numpy as np
import matplotlib.pyplot as plt

data = np.load("100m_times.npy")
x, t = data[:, 0], data[:, 1]
SAMPLES = len(x)

# Constant and linear contributions.
x = np.vstack([np.ones(SAMPLES), x, x ** 2]).T

# Calculate the weights vector.
w = np.dot(np.dot(np.linalg.inv(np.dot(x.T, x)), x.T), t)

quadratic_model = lambda x: w[0] + w[1] * x + w[2] * x ** 2

_fig = plt.figure()
_ax = _fig.gca()
_ax.set_title("Olympic Men's 100m Winning Times")
_ax.set_xlabel("Year")
_ax.set_ylabel("Time (s)")
_ax.scatter(x[:, 1], t, label="Recorded")
_ax.plot(x[:, 1], quadratic_model(x[:, 1]), label="Quadratic Prediction")
_ax.legend(loc="upper right")
plt.show()
   
# From this linear model, we can now predict times.
print(quadratic_model(2022))