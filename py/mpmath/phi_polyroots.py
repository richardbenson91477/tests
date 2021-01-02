#!/usr/bin/env python3
from mpmath import mp
mp.dps = 100

r = mp.polyroots([1,-1,-1])[1]

s = (1 + mp.sqrt(5))/2
print(f"{r}\n{s}\n")

