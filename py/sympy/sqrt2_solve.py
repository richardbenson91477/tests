#!/usr/bin/env python3
import sympy
x = sympy.symbols("x")

f = x * x - 2
s = sympy.solve(f)[1].evalf(100)

print(s)

