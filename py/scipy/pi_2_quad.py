#!/usr/bin/env python3
import scipy
from scipy.integrate import quad

p = quad(lambda x: 4/(1+x*x), 0, 1)[0]

s = scipy.pi
print(f"{p}\n{s}\n")
