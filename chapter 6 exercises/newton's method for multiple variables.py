"""
Does not work. Only iterates once.
Probable sources of errors:
- system of equations
- algorithm
- Jacobian matrix
"""
from numpy import zeros, exp, array
from numpy.linalg import solve


# Let x1 = V1, x2 = V2
def f(x1, x2, i):  # Assume i = N = 2: 2 variables and 2 equations
    # Matrix containing the 2 functions
    matrix1 = [(x1-5)/1000 + x1/4000 + 3e-9*(exp((x1-x2)/0.05)-1), (x2-5)/3000 + x2/2000 + 3e-9*(exp((x1-x2)/0.05)-1)]
    return matrix1[i]


def derivative(x1, x2, i, j):  # jth partial derivative of ith function evaluated at x1 and x2
    epsilon = 0.000000000000001
    # Matrix containing the partial derivatives of the ith function
    matrix2 = [(f(x1+epsilon, x2, i)-f(x1, x2, i))/epsilon, (f(x1, x2+epsilon, i)-f(x1, x2, i))/epsilon]
    return matrix2[j]


N = 2
J = zeros((2, 2))
fmatrix = zeros((2, 1))
x = array([[2], [2]], float)  # Initial point


for counter in range(1):  # Number of iterations
    for i in range(N):
        for j in range(N):
            J[i, j] = derivative(x[0, 0], x[1, 0], i, j)    # Jacobian: jth partial derivative of ith function
    for k in range(N):
        fmatrix[k, 0] = f(x[0, 0], x[1, 0], k)              # Define the f(x) vector
    delta = solve(J, fmatrix)  # Solve for delta x
    x = x - delta  # Define new point
print("V1 is", x[0, 0], "and V2 is", x[1, 0])

