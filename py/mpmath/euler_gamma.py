#!/usr/bin/env python3
from mpmath import mp
mp.dps = 100

b = [1.0 / mp.gamma(x) for x in range(1,71)]
e = sum(b)

s = mp.e
print(f"{e}\n{s}")

