#!/usr/bin/env python3
import numpy as np

# 3 * x + y = 9
# x + 2 * y = 8
a = np.mat([[3, 1], [1, 2]])
b = np.array([9, 8])
s = np.dot(a.I, b)
# a.I == a.getI() == np.linalg.inv(a)
print(s)

