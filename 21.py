a = [1, 2, 3]
i = [x * 2 for x in a]
print(i)
b = [-3, 5, -1, 8, 0, 2]
l = [x for x in b if x>0]
print(l)
wenben = "10 20 30"
p = wenben.split()
o = [float(x) for x in p]
print(o)
jiage = {"苹果": 5, "香蕉": 3, "西瓜": 12, "葡萄": 8}
xin = {x:y for x,y in jiage.items() if y>5}
print(xin)
xin_1 = {x:y+2 for x,y in jiage.items()}
print(xin_1)