from gaussxw import gaussxw
from math import exp


def f(x):
    return exp(-x**2 / (1-x)**2) / (1-x)**2


N = 50
a = 0.0
b = 1

x, w = gaussxw(N)
xp = 0.5*(b-a)*x + 0.5*(b+a)
wp = 0.5*(b-a)*w

s = 0.0
for k in range(N):
    s += wp[k]*f(xp[k])

print(s)