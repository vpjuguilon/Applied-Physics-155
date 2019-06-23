from numpy import linspace
import matplotlib.pyplot as plt


def P(x):
    return 924*x**6 - 2772*x**5 + 3150*x**4 - 1680*x**3 + 420*x**2 - 42*x + 1


def derivative(x):
    return 924*6*x**5 - 2772*5*x**4 + 3150*4*x**3 - 1680*3*x**2 + 420*2*x - 42


x = linspace(0, 1, 100)
y = P(x)
plt.plot(x, y, 'k-')
plt.show()


estimate = [0.0341041, 0.169662, 0.380568, 0.619884, 0.830211, 0.966465]
roots = []

for x in estimate:
    error = 1
    x1 = x
    while error > 1e-10:
        x1, x = x - (P(x)/derivative(x)), x1
        error = abs(x1 - x)
        print('x:', x)
        print('x\':', x1)
        print()
    roots.append(x1)
    print('next root')
print()
print()
print('The roots of the function are', roots)


