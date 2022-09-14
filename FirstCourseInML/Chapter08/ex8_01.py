import numpy as np


x = np.arange(0, 1.01, 0.01)
gam  = 10.0

n = len(x)
k = np.zeros(shape=(n, n))

# Crated the kernel matrix.
for i in range(n):
    for j in range(n):
        k[i, j] = np.exp(-gam * (x[i] - x[j]) ** 2)

k += 1e-6 * np.eye(n)
repmat = np.zeros(shape=(n, 1))
