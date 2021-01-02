#!/usr/bin/env python3
# based on 'solve' docs
from sympy import *
x, y, z = symbols('x y z')
from solve_1b import y1, y2

plot(y1, y2, (x, -5.0, 5.0))

