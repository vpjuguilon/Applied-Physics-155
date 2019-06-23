import numpy as np
import matplotlib.pyplot as plt


def gamma(z):
    value = 1
    for n in range(1, 1000000):
        value *= (1 + (z/n))*np.exp(-z / n)
    return 1 / (z*np.exp(np.euler_gamma*z)*value)


def factorial(number):
    i = number - 1
    while i > 1:
        number *= i
        i += -1
    return number


integx = np.array(np.arange(1, 10, 1))
gammay = gamma(integx+1)
facty_list = []

for j in integx:
    facty_list.append(factorial(j))

facty = np.array(facty_list)
print(facty)
print(gammay)


difference = abs(facty - gammay)
plt.plot(integx, difference, 'b-')
plt.show()

