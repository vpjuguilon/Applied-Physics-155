from numpy import exp
from random import random

def f(x):
    return (x**(-1/2)) / (exp(x) + 1)


def w(x):
    return x**(-1/2)

N = 1000000

summ = 0
for counter in range(N):
    #print(N-counter)
    xi = (random())**2
    summ += 2*f(xi)/w(xi)

print(summ/N)