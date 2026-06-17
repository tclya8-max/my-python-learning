c1 = input("")
c2 = input("")

violet, violet2 = ("красныйсиний"), ("синийкрасный")
orange, orange2 = ("красныйжелтый"), ("желтыйкрасный")
green, green2 = ("синийжелтый"), ("желтыйсиний")
red = ("красныйкрасный")
blue = ("синийсиний")
yellow = ("желтыйжелтый")

res = c1 + c2

if res == violet or res == violet2:
    print("фиолетовый")
elif res == orange or res == orange2:
    print("оранжевый")
elif res == green or  res == green2:
    print("зеленый")
elif res == red:
    print("красный")
elif res == blue:
    print("синий")
elif res == yellow:
    print("желтый")
else:
    print("ошибка цвета")
