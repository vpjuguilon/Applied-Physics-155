prime = []
prime2 = []
checker = 0
i = 1
while len(prime) < 100:
    for j in range (2, i):
        if i%j == 0:
            checker += 1

    if checker == 0:
        prime.append(i)
    checker = 0
    i += 1

for k in prime:
    if k > 50 and k < 100:
        prime2.append(k)

print(prime2)
print(sum(prime2))