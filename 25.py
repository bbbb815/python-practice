while True:
    a = input("输入数据:")
    try:
        b = [int(x) for x in a.split()]
        break
    except ValueError:
        print("不对！")
b = [x for x in b if x >= 0]
c = []
for x in b:
    if x not in c:
        c.append(x)
if c == []:
    print("NO")
else:
    print(",".join(format(x,'b')for x in c))