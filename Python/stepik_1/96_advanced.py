n = int(input())
prev = 1
nex = 1

if n == 1:
    print(1)

elif n == 2:
    print(1, 1)

elif n > 2:
    print(1, 1, end = " ")

    for i in range(n - 2):
        temp = nex
        nex = prev + nex
        print(nex, end = " ")
        prev = temp
