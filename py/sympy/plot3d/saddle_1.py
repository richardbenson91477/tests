#!/usr/bin/env python3
# c/o https://www.youtube.com/watch?v=8aAU4r_pUUU&list=PLSQl0a2vh4HC5feHa6Rc5c0wbRTx56nF7&index=86
from sympy import *

x, y = symbols('x y')

f = x*x - y*y
plotting.plot3d(f)

