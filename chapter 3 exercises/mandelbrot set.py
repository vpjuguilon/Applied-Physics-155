import matplotlib.pyplot as plt
from numpy import linspace

xlist = list(linspace(-2, 2, 1000))
ylist = list(linspace(-2, 2, 1000))

xplot = []
yplot = []
for x in xlist:

    for y in ylist:
        z = 0
        c = complex(x,y)
        for i in range(1, 11):
            z = z**2 + c
        if abs(z) <= 2:
            xplot.append(x)
            yplot.append(y)


plt.plot(xplot, yplot, "k.")
plt.show()

