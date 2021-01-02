#!/usr/bin/env python3
# super fast and perfectly accurate
from mpmath import mp
mp.dps = 100

p = mp.quad(lambda x: 4/(1+x*x), [0, 1])

s = mp.pi
print(f"{p}\n{s}\n")

