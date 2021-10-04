import _tkinter as tk
from functools import partial

def result(label,n1,n2):
    num1=(n1.get())
    num2=(n2.get())
    result=int(num1)+int(num2)
    label.config(text="result = %d" % result)
    return

def result_2(label,n1,n2):
    num1=(n1.get())
    num2=(n2.get())
    result_2=int(num1)-int(num2)
    label.config(text="result = %d" % result)
    return

def result_3(label,n1,n2):
    num1=(n1.get())
    num2=(n2.get())
    result_3=int(num1)*int(num2)
    label.config(text="result = %d" % result)
    return
mee=tk.Tk()
mee.geomtry("400x200")
mee.title("calculator")
number1 = tk.StringVar()
number2 = tk.StringVar()

labelNum1 = tk.Label(root, text="A").grid(row=1, column=0)

labelNum2 = tk.Label(root, text="B").grid(row=2, column=0)

labelResult = tk.Label(root)

labelResult.grid(row=7, column=2)

entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)

entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)

call_result1 = partial(call_result, labelResult, number1, number2)
call_result2 = partial(call_result_2, labelResult, number1, number2)
call_result3 = partial(call_result_3, labelResult, number1, number2)

buttonCal = tk.Button(mee, text="Add", command=call_result1).grid(row=3, column=0)
buttonCal = tk.Button(mee, text="Sub", command=call_result2).grid(row=3, column=2)
buttonCal = tk.Button(mee, text="Mul", command=call_result3).grid(row=3, column=4)

mee.mainloop()


