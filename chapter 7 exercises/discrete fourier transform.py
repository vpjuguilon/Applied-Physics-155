from numpy import linspace, zeros, sin
from cmath import exp, pi
from matplotlib.pyplot import plot, xlabel, ylabel, show, xlim
from random import random

"""""
def square(t):
    error = 1e-10
    output = []
    for i in t:
        if i - 5 < error:
            output.append(0 + random())
        else:
            output.append(10 + random())
    return output
"""

def fsin(t):
    output = []
    for i in t:
        output.append(sin(pi*i*2) + random())
    return output


def dft(y):
    N = len(y)
    c = zeros(N//2 + 1, complex)
    for k in range(N//2 + 1):
        for n in range(N):
            c[k] += y[n]*exp(-2j*pi*k*n/N)
    return c


t = linspace(0, 10, 1000)
y = square(t)
plot(t, y, 'k-')
xlabel('t')
ylabel('y')
show()

c = dft(y)
N = 1000

plot(abs(c), 'r-')
xlim(0, 500)
xlabel('k')
ylabel('c')
show()

