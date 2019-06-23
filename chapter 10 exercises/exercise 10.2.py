from random import random
from numpy import arange
from matplotlib.pyplot import plot, xlabel, ylabel, show, legend

# Constants
Bi213 = 1000
Tl209 = 0
Pb209 = 0
Bi209 = 0
h = 1.0
tmax = 20000

tauPb = 3.3*60
pPb = 1 - 2**(-h/tauPb)
tauTl = 2.2*60
pTl = 1 - 2**(-h/tauTl)
tauBi = 46*60
pBi = 1 - 2**(-h/tauBi)


tpoints = arange(0.0, tmax, h)
Bi213points = []
Tl209points = []
Pb209points = []
Bi209points = []

for t in tpoints:
    Bi213points.append(Bi213)
    Tl209points.append(Tl209)
    Pb209points.append(Pb209)
    Bi209points.append(Bi209)

#Lead decay algorithm
    decay = 0
    for i in range(Pb209):
        if random() < pPb:
            decay += 1
    Pb209 -= decay
    Bi209 += decay

#Thallium decay algorithm
    decay = 0
    for i in range(Tl209):
        if random() < pTl:
            decay += 1
    Tl209 -= decay
    Pb209 += decay

#Bismuth decay algorithm
    decay = 0
    decay1 = 0
    decay2 = 0
    for i in range(Bi213):
        if random() < pBi:
            decay += 1
    Bi213 -= decay
    for i in range(decay):
        if random() < 0.9791:
            decay1 += 1
        else:
            decay2 += 2
    Pb209 += decay1
    Tl209 += decay2



plot(tpoints, Bi213points, 'k-', label='Bismuth-213')
plot(tpoints, Tl209points, 'r-', label='Thallium-209')
plot(tpoints, Pb209points, 'g-', label='Lead-209')
plot(tpoints, Bi209points, 'b-', label='Bismuth-209')
xlabel('Time (s)')
ylabel('Number of atoms')
legend()
show()
