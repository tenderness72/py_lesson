from tkinter import *
from tkinter import ttk
import random
root = Tk()
# Style
s = ttk.Style()
print(s.theme_names())
them_list = ('winnative','clam','alt','default',"classic","vista")
using_theme = them_list[random.randint(0,5)]
s.theme_use('clam')
s.configure('MyWidget.TButton', background='#7374f5')
# Widgets
frame = ttk.Frame(root, padding=(16))
button1 = ttk.Button(
    frame, text='A', style='MyWidget.TButton')
button2 = ttk.Button(
    frame, text='B')
button3 = ttk.Button(
    frame, text='C', style='MyWidget.TButton')
# Layout
frame.pack()
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
# Start
root.mainloop()
