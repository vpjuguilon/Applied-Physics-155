from gaussxw import gaussxw
from numpy import sqrt, linspace
import matplotlib.pyplot as plt


def f(x, amplitude):
    return 1/sqrt(amplitude**3 - x**3)


def period(amplitude):
    a = 0
    b = amplitude
    N = 20

    x, w = gaussxw(N)
    xp = 0.5 * (b - a) * x + 0.5 * (b + a)
    wp = 0.5 * (b - a) * w

    integral = 0.0
    for k in range(N):
        integral += wp[k] * f(xp[k], amplitude)

    return sqrt(8) * integral


T = []
amplitude = list(linspace(0, 20, 100))
for j in amplitude:
    T.append(period(j))

plt.plot(amplitude, T, 'k-')
plt.xlabel("Amplitude (m)")
plt.ylabel("Period (s)")
plt.show()



