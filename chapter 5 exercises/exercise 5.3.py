import numpy as np
import matplotlib.pyplot as plt

def quad(x):
    return np.exp(-x**2)


def integ(x):
    area = 0
    slices = 100
    a = 0
    b = x
    h = (b-a)/slices

    for k in range(1, (slices//2)+1):
        area += (1/3)*h*(quad(a+(2*k-2)*h) + 4*quad(a+(2*k-1)*h) + quad(a+(2*k)*h))

    return area


x_val = np.arange(1, 3.01, 0.01)
y_val = []
for i in x_val:
    y_val.append(integ(i))

plt.plot(x_val, y_val, "k-")
plt.show()


