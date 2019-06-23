from numpy.fft import rfft
from numpy import loadtxt, linspace
from matplotlib.pyplot import plot, show, xlabel, ylabel

datap = loadtxt("piano.txt", float)
datat = loadtxt("trumpet.txt", float)
yp = datap[0:10000]
yt = datat[0:10000]
L = len(yp)
t = linspace(0, L, 1000)

plot(yp, 'r-')
plot(yt, 'b-')
xlabel('t')
ylabel('y')
show()

cp = rfft(yp)
print(len())
ct = rfft(yt)
plot(abs(cp), 'r-')
#plot(abs(ct), 'b-')
show()


