#!/usr/bin/env python3
# c/o https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html#quiver
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

x, y = np.meshgrid(np.arange(-0.8, 1, 0.2), np.arange(-0.8, 1, 0.2))

u = np.sin(np.pi * x) * np.cos(np.pi * y)
v = -np.cos(np.pi * x) * np.sin(np.pi * y)

ax.quiver(x, y, u, v)

plt.show()

