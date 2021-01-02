#!/usr/bin/env python3
from mpmath import mp
mp.dps = 100

n = 242
φ = mp.fib(n) / mp.fib(n-1)

s = (1 + mp.sqrt(5))/2
print(f"{φ}\n{s}\n")

