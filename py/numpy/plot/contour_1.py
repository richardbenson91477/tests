#!/usr/bin/env python3
# c/o https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html#quiver
import matplotlib.pyplot as plt
import numpy as np

#fig, ax = plt.subplots()
x = np.arange(0, np.pi * 2, 0.1)
y = np.arange(0, np.pi * 2, 0.1)
xx, yy = np.meshgrid(x, y)
z = np.sin(xx) - np.cos(yy)
plt.contourf(x,y,z)
plt.show()

