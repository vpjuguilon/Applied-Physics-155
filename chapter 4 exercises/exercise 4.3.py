

def func(x):
    return x*(x-1)


delta = 1e-5
point = float(input("Enter point: "))
derivative = (func(point+delta) - func(point))/delta
print(derivative)

