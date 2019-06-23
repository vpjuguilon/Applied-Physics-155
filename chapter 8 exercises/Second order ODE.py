from numpy import sin, array, pi, arange
from matplotlib.pyplot import plot, show, xlabel

def f(r, t):
    g = 9.81
    l = 0.1
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = -(g/l)*(sin(theta))
    return array([ftheta, fomega], float)


a = 0.0
b = 30.0
N = 1000
h = (b-a)/N

tpoints = arange(a, b, h)
thetapoints = []
wpoints = []

r = array([pi*179/180, 0.0], float)
for t in tpoints:
    thetapoints.append(r[0])
    wpoints.append(r[1])
    k1 = h*f(r, t)
    k2 = h*f(r+0.5*k1, t+0.5*h)
    k3 = h*f(r + 0.5 * k2, t + 0.5 * h)
    k4 = h*f(r+k3, t+h)
    r += (k1+2*k2+2*k3+k4)/6

plot(tpoints, thetapoints, 'k-')
plot(tpoints, wpoints, 'r-')
xlabel('t')
show()






