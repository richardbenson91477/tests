#!/usr/bin/env python3
from mpmath import *

# 3 * x + y = 9
# x + 2 * y = 8
a = matrix([[3, 1], [1, 2]])
b = matrix([9, 8])
ai = a ** -1
s = ai * b

print(s)

