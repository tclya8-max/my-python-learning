m = int(input())
if m == 2:
    print(28)
elif 1 <= m <=7:
    if m % 2 == 0:
        print(30)
    else:
        print(31)
elif 7 < m <= 12:
    if m % 2 == 0:
        print(31)
    else:
        print(30)

