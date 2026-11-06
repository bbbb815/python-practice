import tkinter as tk
def an_le():
    nei_rong = shuru.get()
    jieguo.config(text = "结果是" + nei_rong)
c = tk.Tk()
c.title("我的第一个窗口")
c.geometry("320x220")
tk.Label(c, text="你好").pack()
shuru = tk.Entry(c)
shuru.pack()
jieguo = tk.Label(c,text = "结果显示在这里")
jieguo.pack()
tk.Button(c, text = "按钮", command = an_le).pack()
c.mainloop()