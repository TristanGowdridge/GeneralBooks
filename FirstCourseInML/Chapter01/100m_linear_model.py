# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 13:44:14 2022

@author: trist
"""
import numpy as np
import matplotlib.pyplot as plt

data = np.load("100m_times.npy")
x, t = np.hsplit(data, 2)

# Assuming a linear model, let's calculate the two weights, w0 and w1.
xbar = np.mean(x)
tbar = np.mean(t)
xtbar = np.mean(x * t)
xxbar = np.mean(x * x)
w1 = (xtbar - xbar * tbar) / (xxbar - xbar ** 2)
w0 = tbar - w1 * xbar

linear_model = lambda x: w0 + w1 * x

_fig = plt.figure()
_ax = _fig.gca()
_ax.set_title("Olympic Men's 100m Winning Times")
_ax.set_xlabel("Year")
_ax.set_ylabel("Time (s)")
_ax.scatter(x, t, label="Recorded")
_ax.plot(x, linear_model(x), label="Linear Prediction")
_ax.legend(loc="upper right")
   
# From this linear model, we can now predict times.
print(linear_model(2022))