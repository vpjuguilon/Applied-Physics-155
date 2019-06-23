from numpy import zeros, exp, array
from numpy.linalg import solve


# Let x1 = V1, x2 = V2
def f(x1, x2, i):  # Assume i = N = 2: 2 variables and 2 equations
    # Matrix containing the 2 functions
    matrix1 = [(x1-5)/1000 + x1/4000 + 3e-9*(exp((x1-x2)/0.05)-1), (5-x2)/3000 - x2/2000 + 3e-9*(exp((x1-x2)/0.05)-1)]
    return matrix1[i]


def derivative(x1, x2, i, j):
    # Matrix containing the partial derivatives of the ith function
    matrix2 = [[1/1000 + 1/4000 + 3e-9*(exp((x1-x2)/0.05)-1)*(1/0.05), 3e-9*(exp((x1-x2)/0.05)-1)*(-1/0.05)], [3e-9*(exp((x1-x2)/0.05)-1)*(1/0.05), -1/3000 - 1/2000 + 3e-9*(exp((x1-x2)/0.05)-1)*(-1/0.05)]]
    return matrix2[i][j]


N = 2
J = zeros((2, 2))
fmatrix = zeros((2, 1))
x = array([[0], [0]], float)  # Initial point
print(x)


for counter in range(200):
    for i in range(N):
        for j in range(N):
            J[i, j] = derivative(x[0, 0], x[1, 0], i, j)    # Jacobian: jth partial derivative of ith function
    for k in range(N):
        fmatrix[k, 0] = f(x[0, 0], x[1, 0], k)              # Define the f(x) vector
    delta = solve(J, fmatrix)  # Solve for delta x
    x = x - delta  # Define new point
print(x)

