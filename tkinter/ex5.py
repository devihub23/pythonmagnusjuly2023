from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('250x250')
#v1=IntVar()
#v2=IntVar()
#v3=IntVar()

cb1 = Checkbutton(root,text="Mango",onvalue=1,offvalue=0,height=3,width=10)
cb2 = Checkbutton(root,text="Orange",onvalue=1,offvalue=0,height=3,width=10)
cb3 = Checkbutton(root,text="Apple",onvalue=1,offvalue=0,height=3,width=10)
cb1.pack()
cb2.pack()
cb3.pack()

root.mainloop()
