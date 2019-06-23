from random import random
from numpy import arange
from matplotlib.pyplot import plot, xlabel, ylabel, show, legend

# Constants
NTl = 1000
NPb = 0
tau = 3.053*60
h = 1.0
p = 1 - 2**(-h/tau)
tmax = 1000

tpoints = arange(0.0, tmax, h)
Tlpoints = []
Pbpoints = []

for t in tpoints:
    Tlpoints.append(NTl)
    Pbpoints.append(NPb)


    decay = 0
    for i in range(NTl):
        if random() < p:
            decay += 1
    NTl -= decay
    NPb += decay

plot(tpoints, Tlpoints, 'k-', label='Thalllium')
plot(tpoints, Pbpoints, 'r-', label = 'Lead')
xlabel('Time (s)')
ylabel('Number of atoms')
legend()
show()
