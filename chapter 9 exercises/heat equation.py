from numpy import empty
from matplotlib.pyplot import plot, xlabel, ylabel, show

# Constants
L = 0.01
D = 4.25e-6
N = 100
a = L/N
h = 1e-4
epsilon = h/1000

Tlo = 0.0
Tmid = 20.0
Thi = 50.0

t1 = 0.01
t2 = 0.1
t3 = 0.4
t4 = 1.0
t5 = 50.0
tend = t5 + epsilon

# Create arrays
T = empty(N + 1, float)
T[0] = Thi
T[N] = Tlo
T[1:N] = Tmid
Tp = empty(N+1, float)
Tp[0] = Thi
Tp[N] = Tlo

# Main loop
t = 0.0
c = h*D/(a*a)
while t<tend:

    Tp[1:N] = T[1:N] + c*(T[0:N-1] + T[2:N+1] - 2*T[1:N])
    T, Tp = Tp, T
    t += h

    if abs(t-t1) < epsilon:
        plot(T, 'k-')
    if abs(t-t2) < epsilon:
        plot(T, 'r-')
    if abs(t-t3) < epsilon:
        plot(T, 'g-')
    if abs(t-t4) < epsilon:
        plot(T, 'b-')
    if abs(t-t5) < epsilon:
        plot(T, 'y-')

xlabel('x')
ylabel('T')
show()
