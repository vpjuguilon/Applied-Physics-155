
def quad(x):
    return x**4 - 2*x + 1


def trap(N):
    area = 0
    a = 0
    b = 2
    h = (b-a)/N

    for k in range(1, N+1):
        area += 0.5*h*(quad(a+(k-1)*h)+quad(a+k*h))

    return area


N = 10
I1 = trap(10)
error = 1
final = [[0], [0, I1]]
temp = []
i = 1
counter = 0
draft = []
while counter < 5:
    N *= 2
    i += 1
    temp = []
    temp.append(0)
    print(N)
    temp.append(trap(N))
    print(trap(N))
    for m in range(2, i+1):
        temp.append(temp[m-1] + ((temp[m-1] - final[i-1][m-1])  /   (4**(m-1) - 1)))
    draft = temp
    final.append(draft)
    counter += 1
    print(final)








