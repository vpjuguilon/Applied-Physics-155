from numpy import empty, zeros
from cmath import exp
from matplotlib.pyplot import plot, show, legend
from scipy.constants import hbar
from numpy.linalg import solve
from vpython import sphere, vector, rate


N = 1000
me = 9.109e-31
L = 1e-8
a = L/N
psi = zeros([N, 1], float)
kappa = 5e10
sigma = 1e-10
x0 = L/2
h = 1e-18

for i in range(N):
    x = i*a
    psi[i, 0] = (exp(-((x - x0)**2)/(2*sigma**2))*exp(complex(0, kappa*x))).real

########################################################################
b1 = 1 - h*complex(0, hbar)/(2*me*a**2)
b2 = h*complex(0, hbar)/(4*me*a**2)
v = zeros([N, 1], complex)
for k in range(N):
    if k == 0:
        v[0, 0] = b1*psi[0, 0] + b2*psi[1, 0]
    elif k == N-1:
        v[N-1, 0] = b1*psi[N-1, 0] + b2*psi[N-2, 0]
    else:
        v[k, 0] = b1*psi[k, 0] + b2*(psi[k+1, 0] + psi[k-1, 0])
########################################################################
A = zeros([N, N], complex)
for l in range(N):
    A[l, l] = 1 + h*complex(0, hbar)/(2*me*a**2)
    if l > 0:
        A[l, l-1] = -h*complex(0, hbar)/(4*me*a**2)
        A[l-1, l] = -h*complex(0, hbar)/(4*me*a**2)
#######################################################################
s = empty(N, sphere)
for tcounter in range(10):
    rate(100)
    vnought = solve(A, v)
    for pointcounter in range(N):
        s[pointcounter] = sphere(pos=vector(pointcounter, (vnought[pointcounter]).real, 0), radius=0.2)
    v = vnought
    plot(vnought, label=str(tcounter))
    tcounter += 1
legend()
show()







