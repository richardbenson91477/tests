#!/usr/bin/env python3
import sympy
x = sympy.symbols("x")

f = x*x - x - 1
p = sympy.solve(f)[0].evalf(100)

print(p)

