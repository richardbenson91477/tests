#!/usr/bin/env python3
from sympy import *
x = symbols('x')

print("should throw an error (not print 0):")
print(limit((x - abs(x)) / abs(x),x,0))
