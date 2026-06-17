x = int(input())
l3 = x % 10
l2 = x % 100 // 10
l1 = x // 100
lmax = max(l3, l2, l1)
lmin = min(l3, l2 ,l1)

mid = (l3 + l2 + l1) - lmax - lmin

if lmax - lmin == mid:
    print("Число интересное")
else:
    print("Число неинтересное")
    