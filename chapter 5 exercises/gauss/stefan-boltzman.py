from gaussxw import gaussxw
from math import exp, pi
from scipy.constants import k, c, hbar


def f(x):
    return (x/(1-x))**3 / ((exp(x/(1-x))-1)*(1-x)**2)


N = 4
a = 0.0
b = 1.0

x, w = gaussxw(N)
xp = 0.5*(b-a)*x + 0.5*(b+a)
wp = 0.5*(b-a)*w

s = 0.0
for k in range(N):
    s += wp[k]*f(xp[k])

W = (k**4 * s) / (4*pi**2 * c**2 * hbar**3)
print(W)
