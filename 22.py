a = []
b = []
while True:
    shu_ru = input("输入整数,输入k完成:")
    if shu_ru != "k":
        shu_ru = int(shu_ru)
        a.append(shu_ru)
    else:
        break
while True:
    if a != []:
        c = max(a)
        a.remove(c)
        b.append(str(c))
    else:
        break
print("->".join(b))