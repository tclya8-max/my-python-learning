y_k = int(input())
x_k = int(input())

y = int(input())
x = int(input())

hy = y_k - y
if hy <0:
    hy = y - y_k

hx = x_k - x
if hx <0:
    hx = x - x_k


if hy == 2 and hx == 1:
    print("YES")
elif hy == 1 and hx == 2:
    print("YES")

else:
    print("NO")
    