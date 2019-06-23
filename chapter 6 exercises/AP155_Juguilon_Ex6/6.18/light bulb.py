from numpy import exp, linspace, sqrt
import scipy.constants as sc
import matplotlib.pyplot as plt


def f(x):
    return x**3 / (exp(x) - 1)


def integrate(T):
    kb = sc.k
    h = sc.h
    c = sc.c
    L1 = 390e-9
    L2 = 750e-9
    N = 1000
    a = (h*c) / (L2*kb*T)
    b = (h*c) / (L1*kb*T)

    area = 0
    h = (b - a) / N

    for k in range(1, (N // 2) + 1):
        area += (1 / 3) * h * (f(a + (2 * k - 2) * h) + 4 * f(a + (2 * k - 1) * h) + f(a + (2 * k) * h))
    return area



T = linspace(300, 10000, 10000)
n = []
time = len(T)
for t in T:
    n.append(integrate(t))
    print('Pls wait...', time)
    time -= 1
plt.plot(T, n, 'k-')
plt.show()


accuracy = 1
z = (1 + sqrt(5)) / 2

x1 = 300
x4 = 10000
x2 = x4 - (x4 - x1) / z
x3 = x1 + (x4 - x1) / z

f1 = integrate(x1)
f2 = integrate(x2)
f3 = integrate(x3)
f4 = integrate(x4)

while x4 - x1 > accuracy:
    if f2 > f3:
        x4, f4 = x3, f3
        x3, f3 = x2, f2
        x2 = x4 - (x4 - x1) / z
        f2 = integrate(x2)
    else:
        x1, f1 = x2, f2
        x2, f2 = x3, f3
        x3 = x1 + (x4 - x1) / z
        f3 = integrate(x3)

print("The maximum is", 0.5 * (x1 + x4), "K.")




