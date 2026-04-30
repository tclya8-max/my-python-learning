a = int(input())
a4 = a % 10
a1 = a // 1000
a2 = a // 100 % 10
a3 = a //10 % 10
if a1 + a4 == a2 - a3:
    print("ДА")
else:
    print("НЕТ")
    