#!/usr/bin/env python3
# c/o https://www.goldennumber.net/five-phi/
from mpmath import mp

# 15 works, 16 doesn't

for mp.dps in range(1,100):
    c = 0
    x = mp.mpf('0.0')
    while x <= mp.mpf('1.0'):
        #print(x)
        x += mp.mpf('0.1')
        c += 1
    if c != 11:
        print(f"fails at dps {mp.dps}")

