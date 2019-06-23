from numpy import empty, sin, pi
from matplotlib.pyplot import plot, xlabel, ylabel, show, legend

# Constants
L = 20
D = 0.1
N = 100
a = L/N
h = 0.01
epsilon = h/1000


Tmid = 10.0
Thi = 11.0

t1 = 3375
t2 = 3465
t3 = 3555
t4 = 3645
tend = t4 + epsilon

# Create arrays
T = empty(N + 1, float)
T[0] = Thi
T[1:N] = Tmid
Tp = empty(N+1, float)
Tp[0] = Thi


# Main loop
t = 0.0
c = h*D/(a*a)

while t < tend:
    Tlo = 10 + 12*sin(2*pi*t/365)
    T[N] = Tlo
    Tp[N] = Tlo

    Tp[1:N] = T[1:N] + c*(T[0:N-1] + T[2:N+1] - 2*T[1:N])
    T, Tp = Tp, T
    t += h

    if abs(t-t1) < epsilon:
        plot(T, 'k-', label='March')
    if abs(t-t2) < epsilon:
        plot(T, 'r-', label='June')
    if abs(t-t3) < epsilon:
        plot(T, 'g-', label='September')
    if abs(t-t4) < epsilon:
        plot(T, 'b-', label='December')


xlabel('x')
ylabel('T')
legend()
show()