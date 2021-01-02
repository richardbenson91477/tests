#!/usr/bin/env python3
from mpmath import mp
mp.dps = 100

r = mp.findroot(lambda x: mp.sin(x), 3)

s = mp.pi
print(f"{r}\n{s}\n")

