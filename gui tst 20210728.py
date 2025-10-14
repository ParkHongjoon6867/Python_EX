import sys
from tkinter import *

root  = Tk()
root.title("Park Hong Joon GUI Test")

label1 = Label(root, text="박홍준 입니다.")
label1.pack()

def change():
    label1.config(text="Again, Park Hong Joon !!!")
    
btn = Button(root, text="클릭", command=change)
btn.pack()
    
root.mainloop()