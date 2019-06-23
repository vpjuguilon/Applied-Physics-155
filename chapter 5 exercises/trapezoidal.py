
def quad(x):
    return x**4 - 2*x + 1


def trap(a, b, N):
    area = 0
    h = (b-a)/N

    for k in range(1, N+1):
        area += 0.5*h*(quad(a+(k-1)*h)+quad(a+k*h))

    return area


I1 = trap(0, 2, 100000)
print(I1)
I2 = trap(0, 2, 200000)
print(I2)
error = abs((I2 - I1)/3)
print(error)
print(I2 - error)
