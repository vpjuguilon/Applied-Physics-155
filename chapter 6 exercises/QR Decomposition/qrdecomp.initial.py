# QR Decomposition
# 1) Write a python function that takes as its argument 
# a real square matrix A and returns two matrices Q and
# R that form its QR decomposition
import numpy as np
from numpy.linalg import norm

def decomp(A):
    N = len(A)
    Q = np.zeros((N, N))
    R = np.zeros((N, N))

    for i in range(N):
        summation = 0
        for j in range(i):
            qa = np.dot(Q[:, j], A[:, i])
            summation += qa * Q[:, j]
            R[j, i] = qa
        u = A[:, i] - summation
        q = u/norm(u)

        Q[:, i] = q
        R[i, i] = norm(u)


    return (Q, R)

A = np.array([
    [1, 4, 8, 4],
    [4, 2, 3, 7],
    [8, 3, 6, 9],
    [4, 7, 9, 2],
], dtype=float)
N = len(A)
#print(A)
Q, R = decomp(A)
#print(Q)

# 2) Implement the QR algorithm to calculate the 
# eigenvalues and eigenvectors. Continue calculating 
# until the magnitude of all off-diagonal element is 
# less than 10^-6.

eps = 1e-6
V = np.zeros((N, N))
for i in range(N):   # Identity Matrix
    V[i, i] = 1


offdiag = np.logical_not(np.identity(N))
while (np.abs(A)*offdiag < eps).all() == False:

    Q, R = decomp(A)
    A = np.dot(R, Q)
    V = np.dot(V, Q)




print(A)
print()
print(np.diagonal(A))
print()
print(V)
