def func(x):
    return x**4 - 2*x + 1


def integ(a, b, N):
    area = 0
    h = (b-a)/N

    for k in range(1, (N//2)+1):
        area += (1/3)*h*(func(a+(2*k-2)*h) + 4*func(a+(2*k-1)*h) + func(a+(2*k)*h))
    return area


I1 = integ(0, 2, 1000)
I2 = integ(0, 2, 2000)
print(I2)
error = abs(I1 - I2)/15
print(I2-error)
