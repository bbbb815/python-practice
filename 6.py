class ES:
    def __init__(self, a1, b1, c1, a2, b2, c2):
        self.a1 = a1
        self.b1 = b1
        self.c1 = c1
        self.a2 = a2
        self.b2 = b2
        self.c2 = c2
    def solve(self):
        d = self.a1 * self.b2 - self.a2 * self.b1
        if d == 0:
            return "无解！！！"
        x = (self.c1 * self.b2 - self.c2 * self.b1) / d
        y = (self.a1 * self.c2 - self.a2 * self.c1) / d
        return (x, y)
    def __str__(self):
        return f"方程组: {self.a1}x + {self.b1}y = {self.c1}, {self.a2}x + {self.b2}y = {self.c2}"
    
print("===解二元一次方程组===")
print("\n请输入第一个方程的系数：")
a1 = float(input("a1:"))
b1 = float(input("b1:"))
c1 = float(input("c1:"))
print("\n请输入第二个方程的系数：")
a2 = float(input("a2:"))
b2 = float(input("b2:"))
c2 = float(input("c2:"))
eq = ES(a1,b1,c1,a2,b2,c2)
print("\n您要解的方程组为:")
r = eq.solve()
if type(r)==tuple:
    print(f"解为:x={r[0]}, y={r[1]}")
else:
    print(f"结果：{r}")
with open("二元一次方程组.txt","a",encoding="utf-8") as f:
    f.write(str(eq)+"\n")
    f.write(f"解为:x={r[0]}, y={r[1]}\n\n")
    f.write("====================================\n\n")