from numpy import array, arange
from matplotlib.pyplot import plot, xlabel, show, legend


def f(r, t):
    x = r[0]
    y = r[1]
    z = r[2]
    sigma = 10
    R = 28
    B = 8/3
    fx = sigma*(y-x)
    fy = R*x - y - x*z
    fz = x*y - B*z
    return array([fx, fy, fz], float)


a = 0.0
b = 50.0
N = 5000
h = (b-a)/N

tpoints = arange(a, b, h)
xpoints = []
ypoints = []
zpoints = []

r = array([0.0, 1.0, 0.0], float)  # Initial conditions
for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    zpoints.append(r[2])
    k1 = h*f(r, t)
    k2 = h*f(r+0.5*k1, t+0.5*h)
    k3 = h*f(r + 0.5 * k2, t + 0.5 * h)
    k4 = h*f(r+k3, t+h)
    r += (k1+2*k2+2*k3+k4)/6

plot(tpoints, xpoints, 'r-', label='x')
plot(tpoints, ypoints, 'g-', label='y')
plot(tpoints, zpoints, 'b-', label='z')
xlabel('t')
legend()
show()

plot(xpoints, zpoints, 'k-')
show()


