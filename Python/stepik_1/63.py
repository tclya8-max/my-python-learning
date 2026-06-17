a1 = input()
a2 = input()
a3 = input()

l1 = len(a1)
l2 = len(a2)
l3 = len(a3)

lmax = max(l1, l2 ,l3)
lmin = min(l1, l2, l3)
lmed = (l1 + l2 + l3) - (lmax + lmin)

if lmax + lmin == 2 * lmed:
    print("YES")
else:
    print("NO")
    