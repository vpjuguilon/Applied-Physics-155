from random import random, randrange

counter = 0
N = 1000000
for i in range(N):
    print(N-i)
    dice1 = randrange(1, 7)
    dice2 = randrange(1, 7)
    dice3 = randrange(1, 7)
    if dice1 == 6 and dice2 == 6 and dice3 == 6:
        counter += 1

print(counter/N)
