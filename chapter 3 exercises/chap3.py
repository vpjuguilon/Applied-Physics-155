import matplotlib.pyplot as plt
from numpy import sin, linspace, cos
x = linspace(0,10,100)
y1 = sin(x)
y2 = cos(x)
plt.plot(x,y1,"k-")
plt.plot(x,y2,"k--")
plt.ylim(-1.1,1.1)
plt.xlabel("x axis")
plt.ylabel("y = sin x or y = cos x")
plt.show()