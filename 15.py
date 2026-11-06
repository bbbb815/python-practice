import tkinter as tk
a = {}
def ji():
    qian = float(q.get())
    ci   = p.get()
    a[ci] = qian
    p.delete(0,"end")
    q.delete(0,"end")
def kan():
    he = sum(a.values())
    high_qian = 0
    high_ci = ""
    for bi in a:
        if a[bi] > high_qian:
            high_qian = a[bi]
            high_ci = bi
    jieguo_label.config(text = "总共花了：" + str(he))
    jieguo_label0.config(text = "最高一笔花在了：" + high_ci)

c = tk.Tk()
c.title("花销管理器")
c.geometry("320x320+100+50")
tk.Label(c,text = "这里填备注").pack()
p = tk.Entry(c)
p.pack()
tk.Label(c,text = "这里填金额").pack()
q = tk.Entry(c)
q.pack()
tk.Button(c, text = "记录", command = ji).pack()
tk.Button(c, text = "看记录", command = kan).pack()
jieguo_label = tk.Label(c,text = "")
jieguo_label0 = tk.Label(c,text = "")
jieguo_label.pack()
jieguo_label0.pack()
c.mainloop()