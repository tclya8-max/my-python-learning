# m, n = int(input()), int(input())               Способ через if
# for i in range(m, n - 1, -1):           
#     if not i % 2 == 0:
#         print(i)

# m, n = int(input()), int(input())               Способ без if (преобразуем четное в нечетное и начинаем цикл)

# start = ((m - 1) // 2) * 2 + 1

# for i in range(start, n - 1, -2):
#     print(i)