#!/usr/bin/env python3
# based on 'solve' docs
import math
import numpy as np

r = np.roots([1, -1, -1])[0]

s = (1 + math.sqrt(5)) / 2
print(f"{r}\n{s}\n")

