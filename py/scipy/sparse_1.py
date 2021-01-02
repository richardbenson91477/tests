#!/usr/bin/env python3
# c/o https://machinelearningmastery.com/sparse-matrices-for-machine-learning/
from numpy import array
from scipy.sparse import csr_matrix

# create dense matrix
A = array([[1, 0, 0, 1, 0, 0], [0, 0, 2, 0, 0, 1], [0, 0, 0, 2, 0, 0]])
print(A)
# convert to sparse matrix (CSR method)
S = csr_matrix(A)
print(S)
# reconstruct dense matrix
B = S.todense()
print(B)

