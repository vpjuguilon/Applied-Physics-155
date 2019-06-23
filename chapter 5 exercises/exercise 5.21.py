import numpy as np
from scipy.constants import epsilon_0 as eps
import matplotlib.pyplot as plt

plane = np.zeros((100, 100))

# charges located at 50,45 and 50, 55
for i in range(0, 100):
    for j in range(0, 100):
        if (i == 45 and j == 50) or (i == 55 and j == 50):
            print('skip')
            continue
        r1 = np.sqrt((i-45)**2 + (j-50)**2)
        r2 = np.sqrt((i-55)**2 + (j-50)**2)
        potential1 = +1/(4*np.pi*eps*r1)
        potential2 = -1 /(4*np.pi*eps*r2)
        plane[i, j] = potential1 + potential2


plt.imshow(plane)
plt.colorbar()
plt.jet()
plt.show()
