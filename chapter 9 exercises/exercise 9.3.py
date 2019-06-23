from numpy import empty, zeros, max
from matplotlib.pyplot import imshow, gray, show

# Constants
M = 100
V = 1.0
target = 1e-6

# Create arrays to hold potential values
phi = zeros([M+1, M+1], float)
phi[0, :] = 0
phi[20:80, 20] = 1
phi[20:80, 80] = -1
w = 0.9
# Main loop


while True:
    loopcheck = True
    for i in range(M+1):
        for j in range(M+1):
            if i == 0 or i == M or j == 0 or j == M:
                print('boundary')
            elif i >= 20 and i <= 80 and (j == 20 or j == 80):
                print('line')
            else:
                newpoint = ((1 + w)*(phi[i+1, j] + phi[i-1, j] + phi[i, j+1] + phi[i, j-1]) / 4) - w*phi[i, j]
                if abs(phi[i, j] - newpoint) > target:
                    phi[i, j] = newpoint
                    loopcheck = False
                    print('loopcheck false')
                else:
                    print('loopcheck true')
    print(loopcheck)
    if loopcheck:
        break


imshow(phi)
gray()
show()


