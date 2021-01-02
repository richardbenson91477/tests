#!/usr/bin/env python3
# based on 'solve' docs
import numpy as np

# 3 * x + y = 9
# x + 2 * y = 8
a = np.array ([[3, 1], [1, 2]])
b = np.array ([9, 8])
x = np.linalg.solve (a, b)
print (x)

