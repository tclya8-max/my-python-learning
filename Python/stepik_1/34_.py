w = int(input())
w1 = w - 60
w2 = w - 64
if w1 < 0:
    print("Легкий вес")
elif w2 < 0:
    print("Первый полусредний вес")
else:
    print("Полусредний вес")
