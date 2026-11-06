class jitu:
    def __init__(self, head, foot):
        self.head = head
        self.foot = foot
    def solve(self):
        if self.head == 0:
            return "?"
        else:
            x = (self.foot - 2 * self.head) / 2
            y = self.head - x
            if x < 0 or y < 0:
                return "无解！！！"
            elif x != int(x) or y != int(y):
                return "无解！！！"
            else:
                return (int(x), int(y))
#############################################
print("这是一个解决鸡兔同笼的程序")

h = int(input("请输入总头数："))
f = int(input("请输入总脚数："))
a = jitu(h,f)
r = a.solve()
if type(r)==tuple:
    print(f"鸡有{r[0]}只，兔有{r[1]}只")
else:
    print(r)
