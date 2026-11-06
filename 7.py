name=input("请输入您的姓：")
import math
height=float(input("请输入您的身高（cm）:")) 
neck=float(input("请输入您的脖围（cm）:")) 

records=[] 
while True:
	print("\n===减脂数据管家===")
	print("1.记录今天的bmi和体脂率")
	print("2.查看历史记录")
	print("3.退出")
	choice = input(f"请进行操作，{name}先生：")
	if choice=="1":
		try:
			a=input("输入今日日期：")
			weight=float(input("输入您的今日体重（kg）:")) 
			waist=float(input("输入您的今日腰围（cm）:")) 
			height_m=height/100 
			bmi=weight/(height_m**2) 
			fat_rate=86.01*math.log10(waist-neck)-70.041*math.log10(height)+36.76 
			record={
				"date":a,
				"weight":weight,
				"waist":waist,
				"bmi":round(bmi,2),
				"fat_rate":round(fat_rate,1)
			}
			records.append(record)
			print(f"\n记录成功！")
			print(f"你的BMI是{record['bmi']}")
			print(f"你的体脂率大约是：{record['fat_rate']}%")
			with open("我的减肥日记.txt","a",encoding="utf-8")as f:
				f.write(f"日期:{a}\n")
				f.write(f"体重:{weight}kg\n")
				f.write(f"腰围:{waist}cm\n")
				f.write(f"BMI:{record['bmi']}kg/m^2\n")
				f.write(f"体脂率:{record['fat_rate']}%\n")
				f.write("-"*20+"\n")
			print("数据已保存，继续坚持吧！")
		except ValueError:
			print("错误，你没有输入纯数字！")
	elif choice=="2":
		print("\n===查看历史记录===")
		try:
			with open("我的减肥日记.txt","r",encoding="utf-8")as f:
				content=f.read()
				if content=="":
					print("还没记录，记一条吧！")
				else:
					print(content)
		except FileNotFoundError:
			print("还没记录，记一条吧！")
	elif choice=="3":
		print("拜拜！保持好习惯！")
		break
	else:
		print("输入有误，请输入1，2，3")