from tkinter import *
root1 = Tk()
root1.geometry('250x250')

username = Label(root1,text="Username").grid(row=0,column=0)
t1 = Entry(root1).grid(row=0,column=1)
password = Label(root1,text="Password").grid(row=2,column=0)
t2 = Entry(root1).grid(row=2,column=1)
b1 = Button(root1,text="Login").grid(row=4,column=1)

root1.mainloop()
