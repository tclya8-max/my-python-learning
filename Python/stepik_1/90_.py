n = int(input())
y = 1
e = 1
for i in range(1, n + 1):
    b = e * y
    y = y + 1
    e = b
print(b)


# from math import factorial
# n = int(input())
# print(factorial(n))

#Обычная штука в math