#!/usr/bin/env julia
#using LinearAlgebra

# 3 * x + y = 9
# x + 2 * y = 8
a = [3 1 ; 1 2]
b = [9 ; 8]
ai = inv(a)
s = ai * b

print(s, "\n")

