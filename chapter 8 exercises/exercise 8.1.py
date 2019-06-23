from numpy import arange
from pylab import plot,xlabel,ylabel,show


a = 0.0
b = 10
N = 10000
h = (b-a)/N
tpoints = arange(a, b, h)


def f(x, t):
    if int(2*t) % 2 == 0:
        Vin = 1
    elif int(2*t) % 2 == 1:
        Vin = -1
    RC = 0.001
    return (Vin-x)/RC


Vout = []
x = 0.0
for t in tpoints:
    Vout.append(x)
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1,t+0.5*h)
    k3 = h*f(x+0.5*k2,t+0.5*h)
    k4 = h*f(x+k3,t+h)
    x += (k1+2*k2+2*k3+k4)/6

plot(tpoints, Vout)
xlabel("t")
ylabel("Vout(t)")
show()
