while True:
    a = input("输入:")
    try:
        b = [int(x) for x in a.split()]
        break
    except ValueError:
        print("输入非法！")
c = [x for x in dict.fromkeys(b) if x > 0]
print("NONE" if len(c) == 0 else f"{max(c)},{min(c)}")