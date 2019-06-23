from math import sin
from numpy import array, arange
from matplotlib.pyplot import plot, xlabel, show


def f(r, t):
    x = r[0]
    y = r[1]
    A = 1
    B = 0.5
    C = 0.5
    D = 2
    fx = A*x - B*x*y
    fy = C*x*y - D*y
    return array([fx, fy], float)

a = 0.0
b = 10.0
N = 1000
h = (b-a)/N

tpoints = arange(a, b, h)
xpoints = []
ypoints = []

r = array([2.0, 2.0], float)
for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    k1 = h*f(r, t)
    k2 = h*f(r+0.5*k1, t+0.5*h)
    k3 = h*f(r + 0.5 * k2, t + 0.5 * h)
    k4 = h*f(r+k3, t+h)
    r += (k1+2*k2+2*k3+k4)/6

plot(tpoints, xpoints, 'k-')
plot(tpoints, ypoints, 'r-')
xlabel('t')
show()

