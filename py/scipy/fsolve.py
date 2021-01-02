#!/usr/bin/env python3
import scipy
from scipy.optimize import fsolve
import numpy

r = fsolve(lambda x: numpy.log(x) -1, 1)[0]
s = scipy.e
print(f"ℯ:\n{r}\n{s}\n")

r = fsolve(lambda x: (x*x) -x -1, 1)[0]
s = (1 + numpy.sqrt(5)) / 2
print(f"φ:\n{r}\n{s}\n")

r = fsolve(lambda x: numpy.sin(x), 3)[0]
s = scipy.pi
print(f"π:\n{r}\n{s}\n")

r = fsolve(lambda x: (x * x) - 2, 1)[0]
s = numpy.sqrt(2)
print(f"√2:\n{r}\n{s}\n")

