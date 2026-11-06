import random
import tkinter as tk
c = 0
num = random.randint(1,100)
def kai_shi():
    global c
    guess = s.get()
    try:
        guess = int(guess)
    except ValueError:
        jieguo.config(text = "请重新输入！")
        return
    if guess < 1:
        jieguo.config(text = "请输入1~100的数字")
        return
    if guess > 100:
        jieguo.config(text = "请输入1~100的数字")
        return
    
    if guess > num:
        jieguo.config(text = "大了")
        c+=1
        ci_shu.config(text = f"{c}")
    elif guess < num:
        jieguo.config(text = "小了")
        c+=1
        ci_shu.config(text = f"{c}")
    else:
        jieguo.config(text = "对啦！")
        c+=1
        ci_shu.config(text = f"{c}")
            
def chong_kai():
    global num
    global c
    c = 0
    num = random.randint(1,100)
    jieguo.config(text = "已重开")
    ci_shu.config(text = "0")
a = tk.Tk()
a.title("猜数字")
a.geometry("400x400+400+600")
s = tk.Entry(a)
s.pack()
tk.Button(a, text = "猜一次", command = kai_shi).pack()
tk.Button(a, text = "重开", command = chong_kai).pack()
jieguo = tk.Label(text = "")
jieguo.pack()
ci_shu = tk.Label(text = "")
ci_shu.pack()
a.mainloop()