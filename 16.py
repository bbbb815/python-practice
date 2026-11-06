import tkinter as tk
import random
jie = []
def chu_ti():
    jie.clear()
    try:
        liang = int(s.get())
    except ValueError:
        jieguo.config(text="请输入一个整数！")     
        return
    if liang < 1:
        jieguo.config(text="数量要大于 0！")
        return

    if liang > 100:
        jieguo.config(text="最多 100 道！")
        return
    c = liang + 1
    wenben = ""
    for i in range(1, c):
        p = random.randint(0,100)
        q = random.randint(0,100)
        jie.append((p,q))
        wenben = wenben + f"{i}.x^2-{p+q}x+{p * q}=0\n"
    jieguo.config(text = wenben)
def kan():
    if len(jie) == 0:
        jieguo_0.config(text = "你还没点出题！")
        return
    da_an = ""
    i = 1
    for p,q in jie:
        da_an = da_an +f"第{i}题：答案是{p},{q}\n"
        i+=1
    jieguo_0.config(text = da_an)
a = tk.Tk()
a.title("方程出题器")
a.geometry("400x400")
tk.Label(a, text = "出几道？").pack()
s = tk.Entry(a)
s.pack()
tk.Button(a, text = "出题", command = chu_ti).pack()
jieguo = tk.Label(a, text = "")
jieguo.pack()
tk.Button(a, text = "看答案", command = kan).pack()
jieguo_0 = tk.Label(a,text = "")
jieguo_0.pack()
a.mainloop()