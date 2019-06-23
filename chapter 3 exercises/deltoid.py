import matplotlib.pyplot as plt
from numpy import sin, linspace, cos, pi, exp

#Deltoid
array = linspace(0, 24*pi, 5000)
x = 2*cos(array) + cos(2*array)
y = 2*sin(array) - sin(2*array)
plt.plot(x, y, "k.")
plt.show()

#Galilean Spiral
r = array**2
a = r*cos(array)
b = r*sin(array)
plt.plot(a, b)
plt.show()

#Fey's Function

r = exp(cos(array)) - 2*cos(4*array) + sin(array/12)**5
c = r*cos(array)
d = r*sin(array)
plt.plot(c, d)
plt.show()
