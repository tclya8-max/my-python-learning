a = int(input())
b = int(input())
action = input()
if action == ("/") and b == 0:
    print("На ноль делить нельзя!")
elif action == ("*"):
    print(a * b)
elif action == ("/"):
    print(a / b)
elif action == ("+"):
    print(a + b)
elif action == ("-"):
    print(a - b)
else:
    print("Неверная операция")
    