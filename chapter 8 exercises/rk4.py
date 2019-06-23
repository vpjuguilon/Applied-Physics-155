from math import sin, cos
from numpy import arange, pi, sin, array
from pylab import plot, xlabel, ylabel, show


def f(x,t):
    r = 0.25
    a = 0
    wd = 2/3
    return array([x[1], -r*x[1] - sin(x[0]) + a*cos(x[2]), wd], float)


a = 0.0
b = 10.0
N = 10000
h = (b-a)/N

tpoints = arange(a, b, h)
xArr = []
x = [pi/2, 0, 0]

for t in tpoints:
    xArr.append(x)
    k1 = h*f(x, t)
    k2 = h*f(x+0.5*k1, t+0.5*h)
    k3 = h*f(x+0.5*k2, t+0.5*h)
    k4 = h*f(x+k3, t+h)
    x += (k1+2*k2+2*k3+k4)/6

Phi = []
for element in xArr:
    Phi.append(element[0])

print(xArr)
