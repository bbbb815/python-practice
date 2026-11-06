import tkinter as tk
def jia():
    a = p.get()
    b = q.get()
    try:
        a = float(a)
        b = float(b)
        jieguo.config(text = f"{float(a)} + {float(b)} = {float(a) + float(b)}")
    except ValueError:
        jieguo.config(text = "检查后输入！")
def jian():
    a = p.get()
    b = q.get()
    try:
        a = float(a)
        b = float(b)
        jieguo.config(text = f"{float(a)} - {float(b)} = {float(a) - float(b)}")
    except ValueError:
        jieguo.config(text = "检查后输入！")
def cheng():
    a = p.get()
    b = q.get()
    try:
        a = float(a)
        b = float(b)
        jieguo.config(text = f"{float(a)} x {float(b)} = {float(a) * float(b)}")
    except ValueError:
        jieguo.config(text = "检查后输入！")
def chu ():
    a = p.get()
    b = q.get()

    try:
        a = float(a)
        b = float(b)
        jieguo.config(text = f"{float(a)} / {float(b)} = {float(a) / float(b)}")
    except (ZeroDivisionError,ValueError):
        jieguo.config(text = "检查后输入！")
x = tk.Tk()
x.title("简易计算器")
x.geometry("400x400+300+200")
p = tk.Entry(x)
p.pack()
q = tk.Entry(x)
q.pack()
tk.Button(x, text = "+", command = jia).pack()
tk.Button(x, text = "-", command = jian).pack()
tk.Button(x, text = "x", command = cheng).pack()
tk.Button(x, text = "/", command = chu).pack()
jieguo = tk.Label(x, text = "")
jieguo.pack()
x.mainloop()                                             