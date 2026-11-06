import tkinter as tk
def he():
    piao = {}
    wenben = s.get()
    for x in wenben.split():
        bufen = x.split("：",":")
        piao[bufen[0]] = float(bufen[1])
    zong = sum(piao.values())
    zui_gao_ren = ""
    zui_gao_piao = 0
    for mingzi in piao:
        if piao[mingzi] > zui_gao_piao:
            zui_gao_piao = piao[mingzi]
            zui_gao_ren = mingzi
    jieguo_l.config(text="最高为" + zui_gao_ren + " " + str(zui_gao_piao) + "票")
    jieguo_label.config(text="总票为" + str(zong))
a = tk.Tk()
a.title("班级投票统计系统")
a.geometry("320x220")
s = tk.Entry(a)
s.pack()
tk.Button(a, text = "统计", command = he).pack()
jieguo_label = tk.Label(a, text = "结果显示总和为：")
jieguo_label.pack()
jieguo_l = tk.Label(a, text = "结果显示最高为：")
jieguo_l.pack()
a.mainloop()