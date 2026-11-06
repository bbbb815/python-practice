while True:
    try:
        shu_ru = int(input("输入要转换的:"))
        break
    except ValueError:
        print("打错了，检查！")
print(f"二进制:{format(shu_ru,'b')}")
print(f"八进制:{format(shu_ru,'o')}")
print(f"十六进制:{format(shu_ru,'x')}")