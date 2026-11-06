import math
a = input("您的姓氏是：")
kg = float(input("请输入您的体重（kg）:"))
height = float(input("请输入您的身高（cm）:"))
while True:
    choice = input("请进行您的操作\n1.计算BMI\n2.计算体脂率\n3.退出\n")
    if choice=="1": 
        height_m=height/100 
        bmi=kg/(height_m**2)
        print(f"您的BMI是{bmi:.2f}")
        b = input("是否需要计算体脂率？(y/n):")
        if b == "y":
            neck=float(input("请输入您的脖围（cm）:"))
            waist=float(input("请输入您的腰围（cm）:"))
            fat_rate=86.01*math.log10(waist-neck)-70.041*math.log10(height)+36.76
            print(f"您的体脂率大约是：{fat_rate:.1f}%")
        else:
            print("拜拜！保持好习惯！")
    elif choice=="2":
        neck=float(input("请输入您的脖围（cm）:"))
        waist=float(input("请输入您的腰围（cm）:"))
        fat_rate=86.01*math.log10(waist-neck)-70.041*math.log10(height)+36.76
        print(f"您的体脂率大约是：{fat_rate:.1f}%")
    elif choice=="3":
        print("拜拜！保持好习惯！")
        break
    else:
        print("输入错误，请重新输入！")