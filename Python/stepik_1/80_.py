m, p, n = float(input()), int(input()), int(input())
print(1, m)
n = n - 1
x = 2
for i in range(n):
    print(x, m + (m * (p / 100)))
    x = x + 1
    m = m + (m * (p / 100))
