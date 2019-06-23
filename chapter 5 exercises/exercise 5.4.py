from numpy import cos, sin, pi, linspace
import matplotlib.pyplot as plt

def func(m, x, theta):
    return cos(m*theta - x*sin(theta)) / pi

def integ(m, x):
    area = 0
    slices = 1000
    a = 0
    b = pi
    h = (b-a)/slices

    for k in range(1, (slices//2)+1):
        area += (1/3)*h*(func(m, x, a+(2*k-2)*h) + 4*func(m, x, a+(2*k-1)*h) + func(m, x, a+(2*k)*h))

    return area

xlist = linspace(0, 20, 1000)
ylist = []

m = 0
for x in xlist:
    ylist.append(integ(m, x))
plt.plot(xlist, ylist, "r-")
ylist.clear()

m = 1
for x in xlist:
    ylist.append(integ(m, x))
plt.plot(xlist, ylist, "y-")
ylist.clear()

m = 2
for x in xlist:
    ylist.append(integ(m, x))
plt.plot(xlist, ylist, "g-")
ylist.clear()

m = 3
for x in xlist:
    ylist.append(integ(m, x))
plt.plot(xlist, ylist, "b-")
ylist.clear()

ylist = linspace(0, 0.0000000000000000001, 1000)
plt.plot(xlist, ylist, "k-")
plt.show()
