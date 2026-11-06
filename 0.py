nums=[]
while True:
	a=input("输入数字，输入k取平均值:")
	if a=="k":
		break
	try:
		a = int(a)
	except ValueError:
		print("输入错误请重新输入")
		continue
	nums.append(a)
if len(nums)>0:
	t=sum(nums)
	r=t/len(nums)
	print("平均值是",r)
	print(f"最大值是{max(nums)}")
	print(f"最小值是{min(nums)}")
	shou = 0
	for x in nums:
		shou = shou + x
	if shou == t:
		print("（总和验算通过）")
	else:
		print("（警告：两种算法对不上！）")
else:
	print("你逗我来了？")
	
