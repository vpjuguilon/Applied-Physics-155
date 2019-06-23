import numpy as np

L = int(input("Enter L: "))
madelung = 0

for i in range(-L, L+1):
    for j in range(-L, L+1):
        for k in range(-L, L+1):
            if i == 0 and j == 0 and k == 0:
                continue
            else:
                madelung += ((-1)**(i+j+k))/np.sqrt(i**2 + j**2 + k**2)

print(madelung)
