#!/usr/bin/env python3
from mpmath import mp
p = 100

mp.dps = p * 2
n = mp.power(10, p)
e = mp.power(1 + 1/n, n)
mp.dps = p

s = mp.e
print(f"{e}\n{s}")

