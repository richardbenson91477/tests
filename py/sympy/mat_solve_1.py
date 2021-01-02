#!/usr/bin/env python3
from sympy import *
def main():
    x, y, z = symbols('x y z')
    # 3 * x + y = 9
    # x + 2 * y = 8
    a = Matrix([[3, 1], [1, 2]])
    b = Matrix([9, 8])
    #ai = Inverse(a)
    ai = a.inv()
    s = ai @ b

    print(s)

main()
