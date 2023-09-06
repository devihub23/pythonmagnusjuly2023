from tkinter import *
root = Tk()
root.geometry('250x250')

lb = Button(root,text="Left",height=5,width=10,fg="green")
lb.pack(side=LEFT)
rb = Button(root,text="Right",height=5,width=10,fg="yellow")
rb.pack(side=RIGHT)
tb = Button(root,text="Top",height=5,width=10,fg="blue")
tb.pack(side=TOP)
bb = Button(root,text="Bottom",height=5,width=10,fg="red")
bb.pack(side=BOTTOM)


root.mainloop()
