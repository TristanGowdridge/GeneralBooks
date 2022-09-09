"""
Estimate what sort of values we should expect for the year vs olympic time
plot.

This was done in 100m_linear_model.py.
But from looking at the figure, we should expect the gradient to be negative,
as the running times are decreasing as the year increases. The gradient will 
also be very small as there is only a small decrease in the running time when
compared to an interval of 4 years. If these were plotted on a 1:1 scale the
gradient would be tiny, because of the number of seconds in a year would be
a factor.

The constant offset value is expected to be positive and in the order of 1e2,
as the gradient is so small and the running times are in this magnitude.
"""