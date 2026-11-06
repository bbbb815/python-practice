import tkinter as tk
def tong_ji():
    biao = {}
    wenben = s.get()
    kuai = wenben.split()
    for i in range(0, len(kuai), 2):
        biao[kuai[i]] = float(kuai[i + 1])
    result = sum(biao.values())/len(biao.keys())
    ren = ""
    fen = 0
    for i in biao:
        if biao[i] > fen:
            fen = biao[i]
            ren = i
    min_ren = ""
    min_fen =  float("inf")      
    for l in biao:
        if biao[l] < min_fen:
            min_fen = biao[l]
            min_ren = l
    wenben_jieguo = "平均为" + str(result) + "分\n"
    wenben_jieguo = wenben_jieguo + "最高为" + ren + " " + str(fen) + "分\n"
    wenben_jieguo = wenben_jieguo + "最低为" + min_ren + " " + str(min_fen) + "分"
    jieguo.config(text=wenben_jieguo)
a = tk.Tk()
a.title("成绩统计器")
a.geometry("400x400+300+200")
s = tk.Entry(a)
s.pack()
tk.Button(a, text = "统计", command = tong_ji).pack()
jieguo = tk.Label(a, text = "")
jieguo.pack()
a.mainloop()