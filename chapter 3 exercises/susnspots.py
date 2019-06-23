from numpy import loadtxt
import matplotlib.pyplot as plt
data = loadtxt("sunspots.txt", float)
x = data[:, 0]
y = data[:, 1]
x = x[:1000]
print(len(x))
y = y[:1000]
print(len(y))
plt.plot(x, y)
plt.show()
