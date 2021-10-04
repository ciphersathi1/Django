from tkinter import *
lasi=Tk()
lasi.geometry("200x200")
a=Label(lasi,text="Name").place(x=10,y=20)
c=Label(lasi,text="Password").place(x=10,y=40)

b=Entry(lasi).place(x=70,y=20)
d=Entry(lasi).place(x=70,y=40)

e=Button(lasi,text="Submit").place(x=70,y=60)
lasi.mainloop()


syntax
