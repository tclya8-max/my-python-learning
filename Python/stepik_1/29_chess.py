rook_vertical = int(input())
rook_horizontal = int(input())

turn_vertical = int(input())
turn_horizontal = int(input())

if rook_vertical == turn_vertical or rook_horizontal == turn_horizontal:
    print("YES")
else:
    print("NO")
