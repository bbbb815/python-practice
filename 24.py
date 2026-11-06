while True:
    n = input("输入整数:")
    try:
        n = int(n)
        break
    except:
        print("不对！")
for i in range(1,n+1):
    print("*" * i)