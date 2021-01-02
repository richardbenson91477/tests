#!/usr/bin/env python3
from mpmath import mp
mp.dps = 100

r = mp.findroot(lambda x: mp.log(x) - 1, 1)

s = mp.e
print(f"{r}\n{s}\n")

