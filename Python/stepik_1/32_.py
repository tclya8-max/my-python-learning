a, b, c = int(input()), int(input()), int(input())
if a > b and a > c:
    if b > c:
        print(b)
    elif c > b:
        print(c)
elif b > a and b > c:
    if a > c:
        print(a)
    elif c > a :
        print(c)
else:
    if a > b:
        print(a)
    else:
        print(b)
        