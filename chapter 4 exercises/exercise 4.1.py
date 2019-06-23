from numpy import arange
number = int(input("Enter Number: "))
i = number-1

while i > 1:
    number *= i
    i += -1


print(number)



