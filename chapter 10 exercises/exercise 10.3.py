from vpython import rate, sphere, vec
from random import random


i, j = 0, 0  # Initial
s = sphere(pos = vec(i, j, 0), radius = 0.5)

for counter in range(10000000):
    rate(70)
    s.pos =  vec(i, j, 0)
    z = random()
    if z < 0.25:            # Left
        if i == -50: # Check if boundary
            i = -50
        else:
            i -= 1
    elif 0.25 < z < 0.5:    # Right
        if i == 50: # Check if boundary
            i = 50
        else:
            i += 1
    elif 0.5 < z < 0.75:    # Down
        if j == -50: # Check if boundary
            j = -50
        else:
            j -= 1
    elif 0.75 < z < 1:      # Up
        if j == 50:  # Check if boundary
            j = 50
        else:
            j += 1


