#!/usr/bin/env python3
# based on 'solve' docs
import sympy as sp

x, y, z = sp.symbols('x y z')

# 3 * x + y = 9
l1 = 3 * x + y - 9
y1 = sp.solve(l1, y)[0]
# x + 2 * y = 8
l2 = x + 2 * y - 8
y2 = sp.solve(l2, y)[0]

_x = sp.solve(sp.Eq(y1, y2))[0]
# or y2.subs(x, _x)
_y = y1.subs(x, _x)

print([_x, _y])
