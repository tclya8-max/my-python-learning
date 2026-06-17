from math import log
x = int(input())
b = 0
for i in range(1, x + 1):
    y = 1 / i
    b = b + y

print(b - log(x))
