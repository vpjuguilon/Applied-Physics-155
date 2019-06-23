from gaussxw import gaussxw
from numpy import exp, linspace
from scipy.constants import k
import matplotlib.pyplot as plt


def f(x):
    return (x**4*exp(x)) / (exp(x) - 1)**2


temp = list(linspace(5, 500, 1000))
Cv = []
N = 50
a = 0.0

for T in temp:
    b = 428/T

    x, w = gaussxw(N)
    xp = 0.5 * (b - a) * x + 0.5 * (b + a)
    wp = 0.5 * (b - a) * w

    integral = 0.0
    for k in range(N):
        integral += wp[k] * f(xp[k])

    heat_capacity = 9*0.001*6.022e28*k*((T/428)**3) * integral
    Cv.append(heat_capacity)

print(temp)
print(Cv)
plt.plot(temp, Cv, 'k-')
plt.xlabel('Temperature (K)')
plt.ylabel('Heat Capacity')
plt.show()


