import tkinter as tk
import random as ra
ku = {'石头': -1, '剪刀': 0, '布': 1}
fan = {-1: '石头', 0: '剪刀', 1: '布'}       
win = 0
lose = 0
pin = 0
def bi_sai(player):                          
    global win, lose, pin
    ji = ra.choice(list(ku.values()))        

    if ji == player:                         
        pin += 1                             
        jian = "平局！"
    elif (player == -1 and ji == 0) or (player == 0 and ji == 1) or (player == 1 and ji == -1):
        win += 1
        jian = "你赢了！"
    else:
        lose += 1
        jian = "你输了！"
    jieguo.config(text=f"{jian}\n胜{win} 输{lose} 平{pin}，电脑出了{fan[ji]}")
def shi_tou():
    bi_sai(-1)

def jian_dao():
    bi_sai(0)

def bu():
    bi_sai(1)
c = tk.Tk()
c.title("石头剪刀布！")
c.geometry("400x400+200+300")
tk.Button(c, text = "石头", command = shi_tou).pack()
tk.Button(c, text = "剪刀", command = jian_dao).pack()
tk.Button(c, text = " 布 ", command = bu).pack()
jieguo = tk.Label(c, text = "")
jieguo.pack()
c.mainloop()