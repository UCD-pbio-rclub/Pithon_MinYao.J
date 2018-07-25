# Problem 2
# Create a simple calculator app. Make sure the app can do +,-,/,* at the minimum. Feel free to add more functions which may be found on a calculator.

from tkinter import *

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btn_clear_display():
    global operator
    operator = ""
    text_Input.set("")

def btn_equals_imput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""

cal = Tk()
cal.title("Calculator")
cal.resizable(0, 0)
operator = ""
text_Input = StringVar()


txtDisplay = Entry(cal,font = ('arial', 20, 'bold'), textvariable = text_Input,
                   bd = 30, insertwidth = 4, bg = "light yellow",
                   justify = 'right').grid(columnspan = 4)

btn7 = Button(cal,padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
              text = "7", bg = "pink", command=lambda:btnClick(7)).grid(row = 1, column = 0, sticky=N+S+E+W)

btn8 = Button(cal,padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
              text = "8", bg = "pink", command=lambda:btnClick(8)).grid(row = 1, column = 1, sticky=N+S+E+W)

btn9 = Button(cal,padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
              text = "9", bg = "pink", command=lambda:btnClick(9)).grid(row = 1, column = 2, sticky=N+S+E+W)

Addition = Button(cal,padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
              text = "+", bg = "light goldenrod", command=lambda:btnClick("+")).grid(row = 1, column = 3, sticky=N+S+E+W)

##################################################################################

btn4 = Button(cal,padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
              text = "4", bg = "pink", command=lambda:btnClick(4)).grid(row = 2, column = 0, sticky=N+S+E+W)

btn5 = Button(cal,padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
              text = "5", bg = "pink", command=lambda:btnClick(5)).grid(row = 2, column = 1, sticky=N+S+E+W)

btn6 = Button(cal,padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
              text = "6", bg = "pink", command=lambda:btnClick(6)).grid(row = 2, column = 2, sticky=N+S+E+W)

Subtraction = Button(cal,padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
              text = "-", bg = "light goldenrod", command=lambda:btnClick("-")).grid(row = 2, column = 3, sticky=N+S+E+W)

##################################################################################

btn1 = Button(cal,padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
              text = "1", bg = "pink", command=lambda:btnClick(1)).grid(row = 3, column = 0, sticky=N+S+E+W)

btn2 = Button(cal,padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
              text = "2", bg = "pink", command=lambda:btnClick(2)).grid(row = 3, column = 1, sticky=N+S+E+W)

btn3 = Button(cal,padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
              text = "3", bg = "pink", command=lambda:btnClick(3)).grid(row = 3, column = 2, sticky=N+S+E+W)

Multiply = Button(cal,padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
              text = "*", bg = "light goldenrod", command=lambda:btnClick("*")).grid(row = 3, column = 3, sticky=N+S+E+W)

##################################################################################

btn0 = Button(cal,padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
              text = "0", bg = "pink", command=lambda:btnClick(0)).grid(row = 4, column = 0, sticky=N+S+E+W)

btnclear = Button(cal,padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
              text = "c", bg = "tomato", command=btn_clear_display).grid(row = 4, column = 1, sticky=N+S+E+W)

btnequals = Button(cal,padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
              text = "=", bg = "orange", command=btn_equals_imput).grid(row = 4, column = 2, sticky=N+S+E+W)

Division = Button(cal,padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
              text = "/", bg = "light goldenrod", command=lambda:btnClick("/")).grid(row = 4, column = 3, sticky=N+S+E+W)


cal.mainloop()
