def abc(number):
	number=int(number)
	if number%2==0:
		print("这是一个偶数")
	else:
		print("这是一个奇数")
while True:
	a=input("请输入要判断的数字按q退出：")
	if a=="q":
		print("我走了，你别太难过~")
		break
	try:
		b=int(a)
		abc(b)
	except ValueError:
		print("你在逗我吗？")