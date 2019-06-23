import matplotlib.pyplot as plt
from numpy import linspace, zeros, log

xlist = linspace(-2, 2, 1000)
ylist = linspace(2, -2, 1000)
arrayplot = zeros((1000, 1000))

j = 0
for y in ylist:
    i = 0
    for x in xlist:
        z = 0
        c = complex(x, y)
        n = 0

        while abs(z) <= 2:   #Check for number of iterations before |z| > 2 or if max iterations (11)
            z = z**2 + c
            n += 1
            if n == 50:
                break

        arrayplot[j, i] = n
        i += 1
    j += 1


plt.imshow(arrayplot)
plt.jet()
plt.show()





