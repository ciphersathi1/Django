import tkinter as tk  
from functools import partial
   
   
def call_result1(label_result, n1, n2):  
    num1 = (n1.get())  
    num2 = (n2.get())  
    result = int(num1)+int(num2)  
    label_result.config(text="Result = %d" % result)  
    return  

def call_result2(label_result, n1, n2):  
    num1 = (n1.get())  
    num2 = (n2.get())  
    result = int(num1)-int(num2)  
    label_result.config(text="Result = %d" % result)  
    return

def call_result3(label_result, n1, n2):  
    num1 = (n1.get())  
    num2 = (n2.get())  
    result = int(num1)*int(num2)  
    label_result.config(text="Result = %d" % result)  
    return

root = tk.Tk()  
root.geometry('400x200+100+200')  
  
root.title('Calculator')  
   
number1 = tk.StringVar()  
number2 = tk.StringVar()  
  
labelNum1 = tk.Label(root, text="A").grid(row=1, column=0)  
  
labelNum2 = tk.Label(root, text="B").grid(row=2, column=0)  
  
labelResult = tk.Label(root)  
  
labelResult.grid(row=7, column=2)  
  
entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)  
  
entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)  
  
call_result1 = partial(call_result1, labelResult, number1, number2)
call_result2 = partial(call_result2, labelResult, number1, number2)
call_result3 = partial(call_result3, labelResult, number1, number2) 
  
buttonCal = tk.Button(root, text="Add", command=call_result1).grid(row=3, column=0)
buttonCal = tk.Button(root, text="Sub", command=call_result2).grid(row=3, column=2)
buttonCal = tk.Button(root, text="Mul", command=call_result3).grid(row=3, column=4)
  
root.mainloop()  
