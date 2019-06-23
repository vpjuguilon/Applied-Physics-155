from numpy import loadtxt, zeros
from cmath import exp, pi
from matplotlib.pyplot import plot, xlabel, ylabel, show


def dft(y):
    N = len(y)
    c = zeros(N//2+1, complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*exp(-2j*pi*k*n/N)
    return c


data = loadtxt("sunspots.txt", float)
t = data[:, 0]
y = data[:, 1]
c = dft(y)
print(len(t))
plot(t, y, 'k-')
xlabel('t')
ylabel('y')
show()


plot(abs(c), 'r.')
xlabel('k')
ylabel('c')
show()




