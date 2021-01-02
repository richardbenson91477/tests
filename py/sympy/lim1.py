#!/usr/bin/env python3
from sympy import *
x = symbols('x')

print(limit(sin(x) / x, x, 0))

