k1, k2 = int(input()), int(input())
k3, k4 = int(input()), int(input())

if (k1 + k2) % 2 == 0 and (k3 + k4) %2 == 0:
    print("YES")
elif (k1 +k2) %2 != 0 and (k3 + k4) %2 != 0:
    print("YES")
else:
    print("NO")
