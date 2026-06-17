y_s = int(input())
x_s = int(input())

y = int(input())
x = int(input())

hy = y_s - y
if hy <0:
    hy = y - y_s

hx = x_s - x
if hx <0:
    hx = x - x_s


if hy == hx:
    print("YES")
elif hy != hx:
    if hx == 0 or hy == 0:
        print("YES")
    else:
        print("NO")

