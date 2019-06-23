import matplotlib.pyplot as plt
from numpy import linspace, sqrt, tan
from scipy.constants import m_e, e, hbar

ev = linspace(0, 20, 1000)
E = ev * e
w = 1e-9
V = 20*e
me = m_e
y1 = []
y2 = []
y3 = []
for k in E:
    y1.append(tan(sqrt((w**2 * me * k) / (2*hbar**2))))
for i in E:
    y2.append(sqrt((V-i)/i))
for j in E:
    y3.append(-sqrt(j / (V - j)))


plt.plot(E, y1, 'k-')
plt.plot(E, y2, 'r-')
plt.plot(E, y3, 'b-')
plt.show()
