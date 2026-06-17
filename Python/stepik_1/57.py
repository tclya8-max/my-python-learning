a = int(input())
b = int(input())
c = int(input())
mid = (a + b + c) - max(a, b, c) - min(a, b, c)

print(max(a, b, c))
print(mid)
print(min(a, b, c))
