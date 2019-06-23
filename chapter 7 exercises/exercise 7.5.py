from numpy import linspace
from numpy.fft import rfft, irfft
from matplotlib.pyplot import plot, show


def f(t):
    output = []
    for i in t:
        if int(i*2) % 2 == 0:
            output.append(1)
        else:
            output.append(-1)
    return output


t = linspace(0, 1, 1000)
y1 = f(t)
c = rfft(y1)
for j in range(10, len(c)):
    c[j] = 0
y2 = irfft(c)
plot(y1, 'k-')
plot(y2, 'r-')
show()



