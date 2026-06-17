n = int(input())
if n == 0:
    print("зеленый")
if 1 <= n <= 10:
    if n % 2 == 0:
        print("черный")
    else:
        print("красный")
elif 11 <= n <= 18:
    if n % 2 == 0:
        print("красный")
    else:
        print("черный")
elif 19 <= n <= 28:
    if n % 2 == 0:
        print("черный")
    else:
        print("красный")
elif 29 <= n <= 36:
    if n % 2 == 0:
        print("красный")
    else:
        print("черный")
elif n != 0:
    print("ошибка ввода")
