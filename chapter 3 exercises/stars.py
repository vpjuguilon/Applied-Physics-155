import matplotlib.pyplot as plt
from numpy import loadtxt
data = loadtxt("stars.txt",float)
x = data[:,0]
y = data[:,1]
plt.scatter(x,y)
plt.xlabel("Temperature")
plt.ylabel("Magnitude")
plt.xlim(13000, 0)
plt.ylim(20, -5)
plt.show()