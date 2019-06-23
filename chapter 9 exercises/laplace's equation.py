from numpy import empty, zeros, max
from matplotlib.pyplot import imshow, gray, show

# Constants
M = 100
V = 1.0
target = 1e-4

# Create arrays to hold potential values
phi = zeros([M+1, M+1], float)
phi[0, :] = V
phiprime = empty([M+1, M+1], float)
w = -2

# Main loop
delta = 1.0
while delta > target:
    for i in range(M+1):
        for j in range(M + 1):
            if i == 0 or i == M or j == 0 or j == M:
                phiprime[i, j] = phi[i, j]
            else:
                phiprime[i, j] = (phi[i+1, j] + phi[i-1, j] + phi[i, j+1] + phi[i, j-1]) / 4

    delta = max(abs(phi-phiprime))
    phi, phiprime = phiprime, phi
    print(delta)

imshow(phi)
gray()
show()


