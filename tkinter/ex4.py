from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('250x250')

def m1():
    text = "You have Clicked the Button"
    messagebox.showinfo("Message",text)

b1 = Button(root,text="Click",command=root.destroy)

b1.pack()

root.mainloop()
