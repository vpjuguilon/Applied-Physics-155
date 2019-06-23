from numpy import exp, arange
import matplotlib.pyplot as plt


def f(x, c):
    return 1 - exp(-c*x)


def fprime(x):
    return (2*exp(-2*x))


C = arange(0, 3, 0.01)
y = []
for c in C:
    x1 = 1
    accuracy = 1e-6
    error = 1
    while error > accuracy:
        x1, x2 = f(x1, c), x1
        error = abs((x2 - x1) / (1 - 1 / (fprime(x2))))
    y.append(x1)

plt.plot(C, y, 'k-')
plt.show()
