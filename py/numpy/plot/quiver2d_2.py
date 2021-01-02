#!/usr/bin/env python3
# c/o https://www.tutorialspoint.com/matplotlib/matplotlib_quiver_plot.htm
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

x, y = np.meshgrid(np.arange(-2, 2, 0.2), np.arange(-2, 2, 0.25))

z = x * np.exp(-x**2 - y**2)
v, u = np.gradient(z, 0.2, 0.2)

ax.quiver(x, y, u, v)

plt.show()

