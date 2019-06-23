import matplotlib.pyplot as plt
from numpy import loadtxt
data = loadtxt("circular.txt",float)
print(data)
plt.imshow(data, origin="lower", extent=[0,10,0,5])
plt.jet()
plt.colorbar()
plt.show()

