import random
from tkinter import *
from tkinter.ttk import *
import tkinter.ttk as ttk
from ttkthemes import *

'''
def get_huda(huda):
    you = huda
    frame3.tkraise()
    cpu = random.choice(['グー','チョキ','パー'])
    kekka['text']=('%svs%s'%(you,cpu))

def test():
    root.destroy()

def tehuda():
    frame3.tkraise()
'''

#メインウィンドウ
root = Tk()

style = ttk.Style()
style.theme_names()
style.theme_use('clam')
style.configure('MyWidget.TButton', background='#f7e07c')

root.title('ジャンケン')
root.geometry('300x200')
#メインウィンドウのグリッドを1×1にする
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

#メインフレームの作成と設置
frame1 = ttk.Frame(root)
frame1.grid(row=0, column=0, sticky='nsew', pady=20)
#アプリフレームの作成と設置
frame2 = ttk.Frame(root)
frame2.grid(row=0, column=0, sticky='nsew', pady=20)
#アプリフレームの作成と設置
frame3 = ttk.Frame(root)
frame3.grid(row=0, column=0, sticky='nsew', pady=20)
#アプリフレームの作成と設置
frame4 = ttk.Frame(root)
frame4.grid(row=0, column=0, sticky='nsew', pady=20)

#挑戦ダイアログ（ジャンケンをしましょう。受けて立つor遠慮いたします）
tyosen = ttk.Label(frame1, text='ジャンケンをしましょう！！', font=("Times", 15))
tyosen.pack()
tyosen_true = ttk.Button(frame1, text='受けて立つ', width=15, style='MyWidget.TButton', command=frame2.tkraise)
tyosen_true.pack(padx=20,side='left')
tyosen_false = ttk.Button(frame1, text='遠慮致します', width=15, style='MyWidget.TButton', command=root.destroy)
tyosen_false.pack(padx=20,side='right')


#ジャンケンダイアログ（グーorチョキorパー）
you_huda = ttk.Label(frame2, text='あなたの手札を選んでください', font=("Times", 10))
you_huda.pack()
you_huda_gu = ttk.Button(frame2, text='グー', width=10, command=lambda:get_huda('グー'), style='MyWidget.TButton')
you_huda_gu.pack(pady=15, side='top')
you_huda_tyoki = ttk.Button(frame2, text='チョキ', width=10, command=lambda:get_huda('チョキ'), style='MyWidget.TButton')
you_huda_tyoki.pack(padx=30, side='left')
you_huda_pa = ttk.Button(frame2, text='パー', width=10, command=lambda:get_huda('パー'), style='MyWidget.TButton')
you_huda_pa.pack(padx=30, side='right')


#関数
def get_huda(you_huda):
    f=open('./game.log',mode='a',encoding='utf-8')
    #you = huda
    frame3.tkraise()
    cpu = random.choice(['グー','チョキ','パー'])
    if you_huda==cpu:
        syohai='あいこ'
        kekka_ok.pack_forget()
        kekka_aiko.pack(pady=15)
        f.write('retry,')
    elif (you_huda=='グー' and cpu=='チョキ') or (you_huda=='チョキ' and cpu=='パー')or (you_huda=='パー' and cpu=='グー'):
        syohai='あなたの勝ち'
        kekka_aiko.pack_forget()
        kekka_ok.pack(pady=15)
        f.write('win\n')
    else:
        syohai='あなたの負け'
        kekka_aiko.pack_forget()
        kekka_ok.pack(pady=15)
        f.write('lose\n')
    kekka['text']=('%svs%s\n%s'%(you_huda,cpu,syohai))
    f.close()
    print('ログを保存しました。')


#勝敗ダイアログ（あなたvsCPU 勝敗引き分け）
kekka = ttk.Label(frame3, text='勝負')
kekka.pack()
kekka_ok = Button(frame3, text='OK', width=10, command=frame4.tkraise)
kekka_aiko = Button(frame3, text='あいこでしょ', width=10, command=frame2.tkraise)
kekka_ok.pack(pady=15)

#再戦or終了ダイアログ
saisen = ttk.Label(frame4, text='もう一度ジャンケンしますか？')
saisen_true = ttk.Button(frame4, text='再戦', width=4, command=frame2.tkraise, style='MyWidget.TButton')
saisen_true.pack(padx=30, side='left')
saisen_false = ttk.Button(frame4, text='終了', width=4, command=root.destroy, style='MyWidget.TButton')
saisen_false.pack(padx=30, side='right')

frame1.tkraise()
root.mainloop()
