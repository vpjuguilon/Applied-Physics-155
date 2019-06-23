import numpy as np
import matplotlib.pyplot as plt
from math import gamma

def testgamma(z):
    value = 1
    for n in range(1, 1000000):
        value *= (1 + (z/n))*np.exp(-z / n)
    return 1 / (z*np.exp(np.euler_gamma*z)*value)



integx = np.array(np.arange(1, 10, 1))
gammay1 = testgamma(integx+1)
gammay2 = gamma(integx+1)

print(gammay2)
print(gammay1)

plt.plot(integx, gammay1, 'k-')
plt.plot(integx, gammay2, 'r-')
plt.show()

difference = abs(gammay2 - gammay1)
plt.plot(integx, difference, 'b-')
plt.show()

