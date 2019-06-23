from numpy import arange
import matplotlib.pyplot as plt
xlist = []
ylist = list(arange(1, 4.01, 0.001))


for r in ylist:
    x = 0.5
    for j in range(1, 100):
        x = r*x*(1-x)
    for k in range(1, 100):
        x = r*x*(1-x)
    xlist.append(x)

print(xlist)
print(ylist)
plt.plot(ylist, xlist, "k.")
plt.xlabel("r")
plt.ylabel("x at 1000")
plt.show()


