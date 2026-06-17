n1 = input()
n2 = input()
n3 = input()

l1 = len(n1)
l2 = len(n2)
l3 = len(n3)
lmax = max(l1, l2, l3)
lmin = min(l1, l2, l3)

if l1 == lmin:
    print(n1)
    if l2 == lmax:
        print(n2)
    else:
        print(n3)
elif l2 == lmin:
    print(n2)
    if l1 == lmax:
        print(n1)
    else:
        print(n3)
elif l3 == lmin:
    print(n3)
    if l1 == lmax:
        print(n1)
    else:
        print(n2)
        