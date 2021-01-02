#!/usr/bin/env python3
# c/o mpmath.org
from mpmath import mp
mp.dps = 100

p = mp.quad(lambda x: mp.exp(-x**2), [-mp.inf, mp.inf]) ** 2

s = mp.pi
print(f"{p}\n{s}\n")

