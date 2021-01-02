#!/usr/bin/env python3
from mpmath import mp
mp.dps = 100

r = mp.polyroots([1,0,-2])[1]

s = mp.sqrt(2)
print(f"{r}\n{s}\n")

