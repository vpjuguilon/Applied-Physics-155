from numpy import sin, arange
from matplotlib.pyplot import plot, show, xlabel, ylabel


def f(x, t):
    return -x**3 + sin(t)


xpoints = []
h = 10/1000
tpoints = arange(0, 10, h)
x = 0

for t in tpoints:
    xpoints.append(x)
    x += h*f(x, t)

plot(tpoints, xpoints, 'k-')
xlabel('t')
ylabel('x(t)')
show()



