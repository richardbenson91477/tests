#!/usr/bin/env python3
# based on 'solve' docs
from sympy import *
x, y, z = symbols('x y z')

# 3 * x + y = 9
l1 = 3 * x + y - 9
# x + 2 * y = 8
l2 = x + 2 * y - 8

s = solve([l1, l2], [x, y])

print(s)

