import numpy as np
import matplotlib.pyplot as plt


def gamma(z):
    value = 1
    for n in range(1, 1000000):
        value *= (1 + (z/n))*np.exp(-z / n)
    return 1 / (z*np.exp(np.euler_gamma*z)*value)


x = np.linspace(-4, 5, 100)
y = gamma(x)


fig, ax = plt.subplots()
ax.plot(list(x), list(y), 'k-')
plt.ylim(ymin=-6, ymax=6)
plt.xlim(xmin=-6, xmax=6)
ax.set_aspect('equal')
ax.grid(True, which='both')
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
plt.show()


