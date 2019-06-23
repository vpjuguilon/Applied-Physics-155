Cn = 1
C = [1]
A = []
n = 0
Am = 0

for i in range(1, 510):
    C.append(Cn)
    n += 1
    Cn *= (4*n + 2)/(n + 2)

print(C)
print(C[499])









