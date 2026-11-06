def du_shuzi(tishi):
    while True:
        try:
            return int(input(tishi))
        except ValueError:
            print("输入错误，请重新输入！")
c=0
import random
num=random.randint(1, 100)
a = du_shuzi("请输入一个整数：")
while True: 
    if a>num:
        print("你输入的数字大于随机数")
        a = du_shuzi("请输入一个整数：")
        c+=1
    elif a<num:
        print("你输入的数字小于随机数")
        a = du_shuzi("请输入一个整数：")
        c+=1
    else:
        print(f"恭喜你猜对啦，你猜了{c}次,正确答案是{num}")
        break




