#!/usr/bin/env python3
import numpy as np

def similar (v1, v2):
    ε = 0.000001
    # is this accurate enough? seems reasonable
    if np.linalg.norm(v1 - v2) < ε:
        return True;
    #if abs(v1[0] - v2[0]) < ε and \
    #        abs(v1[1] - v2[1]) < ε and \
    #        abs(v1[2] - v2[2]) < ε:
    #    return True
    return False

# values c/o https://www.youtube.com/watch?v=tmCLteLe21I
A = np.array([[3, 6, 7],
              [3, 3, 7],
              [5, 6, 5]])

# vector to test whether an eigenvector of A
b = np.array([[ 1],
              [-2],
              [ 1]])

# get normalized eigenvalues and eigenvectors of A
λ, v = np.linalg.eig(A)
# create vc from v's columns because v is ordered column-wise
vc = [v[:,i] for i in range(3)]

# make b a vector
bv = b.reshape([1,3])[0]
# normalize
bv_n = bv / np.linalg.norm(bv)

for i in range (3):
    if similar(bv_n, vc[i]):
        print(f"{b}\n matches eigenvector\n {vc[i].reshape([3,1])}")

