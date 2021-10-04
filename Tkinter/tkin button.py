from tkinter import *   
  
top = Tk() 
  
top.geometry("200x100")  

def fun():  
    messagebox.showinfo("Hello", "Red Button clicked")  
  
  
b1 = Button(top,text = "Red",command=fun() ,activeforeground = "black",activebackground = "red",pady=0)  
  
b2 = Button(top, text = "Blue",activeforeground = "black",activebackground = "blue",pady=10)  
  
b3 = Button(top, text = "Green",activeforeground = "black",activebackground = "green",pady = 10)  
  
b4 = Button(top, text = "Yellow",activeforeground = "black",activebackground = "yellow",pady = 10)  
  
b1.pack(side = LEFT)  
  
b2.pack(side = RIGHT)  
  
b3.pack(side = TOP)  
  
b4.pack(side = BOTTOM)  
  
top.mainloop()  
