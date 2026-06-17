n = int(input())

a = int(input())
b = int(input())

min_ab = min(a, b)
max_ab = max(a, b)

for i in range(n - 2):
    c_input = int(input())
    if c_input > min_ab and c_input > max_ab:
        min_ab = max_ab
        max_ab = c_input
    elif c_input > min_ab:
        min_ab = c_input

print(max_ab)
print(min_ab)
