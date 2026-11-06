def one(a):
    while True:
        try:
            a = int(a)
            break
        except ValueError:
            print("重试")
    return(a**2)
#########################################
def two(b):
    while True:
        try:
            b = int(b)
        except ValueError:
            print("重试")
        if b <= 0:
            print("重试")
        else:
            break
    if b % 2 == 0:
        return("偶数")
    else:
        return("奇数")
#########################################
def three(n):
    p = []
    while True:
        try:
            n = int(n)
        except ValueError:
            print("重试")
        if n < 1 or n > 1000:
            print("超出范围")
        else:
            break
    for i in range (1,n+1):
        p.append(i)
    return(sum(p))
#########################################
def four():
    while True:
        x = input("输入")
        try:
            y = [int(i) for i in x.split()]
        except ValueError:
            print("重试")
            continue
        if len(y) != 2:
            print("重试")
            continue
        elif y[1] == 0:
            print("除数不能为0，重试")
            continue
        else:
            break
    return(f"{y[0]//y[1]},{y[0]%y[1]}")
#########################################
def five():
    while True:
        a = input("输入")
        try:
            p = [float(i) for i in a.split()]
        except ValueError:
            print("重试")
            continue
        if len(p) == 0:
            print("重试")
            continue
        break
    return round(sum(p) / len(p),2)
#########################################
while True:
    choice = input("第几道题(k退出)：")
    
    if choice =="4":
        print(four())
    elif choice =="5":
        print(five())
    elif choice =="k":
        break
    else:
        print("不对")
