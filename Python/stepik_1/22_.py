a1 = int(input())
a2 = int(input())
a3 = int(input())
a4 = int(input())

a1_2 = 0
a3_4 = 0

if a1 <= a2:
    a1_2 = a1_2 + a1
else:
    a1_2 = a1_2 + a2

if a3 <= a4:
    a3_4 = a3_4 + a3
else:
    a3_4 = a3_4 + a4

if a1_2 <= a3_4:
    print(a1_2)
else:
    print(a3_4)
