#!/usr/bin/env python3
from mpmath import mp
mp.dps = 100

five = 5.0
print(f"{five}")

sqrt_five = mp.sqrt(five)
φ = (1.0 + sqrt_five) / 2.0
print(f"{φ}")

n = 242
f1 = mp.nint(mp.power(φ, n) / sqrt_five)
f2 = mp.nint(mp.power(φ, n - 1) / sqrt_five)
φb = f1 / f2
print(f"{φb}")

five_b = mp.power(φb * 2.0 - 1.0, 2.0)
print(f"{five_b}")

