from numpy.fft import rfft, irfft
from numpy import loadtxt, linspace
from matplotlib.pyplot import plot, show, xlabel, ylabel

data = loadtxt("dow.txt", float)
L = len(data)
c = rfft(data)
N = len(data)//2 + 1
# for i in range(int(0.10*N), N):
#    c[i] = 0

plot(abs(c), 'k-')
# data2 = irfft(c)
# plot(data, 'k-')
# plot(data2, 'r-')
show()
