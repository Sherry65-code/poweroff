from os import system
from tkinter import Tk, Label, Button
from sys import exit
def explitexit():
    exit()
def poweroff():
    if (system("poweroff") == 0):
        pass
    else:
        system("pkexec poweroff")
root = Tk()
root.overrideredirect(True)
root.geometry("250x120+525+300")
root.maxsize(width=250, height=120)
root.minsize(width=250, height=120)
root.config(bg="#16171a")
f1 = ("Arial", 20)
l1 = Label(font=("Arial",10), bg="#16171a", fg="white", text="Do you really wanna say Goodbye?")
l1.pack(pady=10)
b1 = Button(text="Yes", bg="#47494f", fg="white", font=("Arial",10), relief="flat", borderwidth=0, highlightthickness=0, width=10 , height=1, command=poweroff)
b2 = Button(text="No", bg="#47494f", fg="white", font=("Arial",10), relief="flat", borderwidth=0, highlightthickness=0, width=10  , height=1, command=explitexit)
b1.pack()
b2.pack(pady=8)
root.mainloop()
