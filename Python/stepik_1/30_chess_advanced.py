x_king = int(input())
y_king = int(input())

x = int(input())
y = int(input())

if x_king - 1 <= x <= x_king + 1 and y_king - 1 <= y <= y_king + 1:
    print("YES")
else:
    print("NO")
