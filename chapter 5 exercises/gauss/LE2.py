from matplotlib.pyplot import plot, show
from numpy import sqrt, exp, pi, linspace
from math import factorial

L = 100000


# Hermitian Function
def H(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return 2 * x
    else:
        return 2 * x * H(n - 1, x) - 2 * (n - 1) * H(n - 2, x)


# Psi(x)
def fPsi(n, x):
    return (exp(-0.5 * x ** 2) * H(n, x)) / (sqrt(2 ** n * factorial(n) * sqrt(pi)))


def integrand(x):
    return (x**2) * (fPsi(5, x))**2


def integ(a, b, N):
    area = 0
    h = (b-a)/N

    for k in range(1, (N//2)+1):
        area += (1/3)*h*(integrand(a+(2*k-2)*h) + 4*integrand(a+(2*k-1)*h) + integrand(a+(2*k)*h))
    return area


X = linspace(-10000, 10000, 1000)
Y = []
for var in X:
    Y.append(integrand(var))

plot(X, Y, 'k-')
show()

