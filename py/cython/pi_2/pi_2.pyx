#!/usr/bin/env python3
#from libc.math cimport sqrt

def pi_2():
    cdef long num_steps = 10 ** 9
    cdef double step = 1.0 / num_steps

    cdef double total = 0.0
    cdef double i = 0
    for i in range(num_steps):
        total += 4.0 / (1.0 + ((i + 0.5) * step)**2)

    return step * total

