from tkinter import *


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)


def btnClearDisplay():
    global operator
    operator = ''
    text_input.set('')


def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)


cal = Tk()
cal.title('Calculator')
operator = ''
text_input = StringVar()

txtDisplay = Entry(cal, textvariable=text_input, bd=30, insertwidth=4,
                   bg='grey', justify='right').grid(columnspan=4)

btn7 = Button(cal, padx=16, bd=5, fg='white', font=('arial', 20),
              text="7", bg='grey', command=lambda: btnClick(7)).grid(row=1, column=0)
btn8 = Button(cal, padx=16, bd=5, fg='white', font=('arial', 20),
              text="8", bg='grey', command=lambda: btnClick(8)).grid(row=1, column=1)
btn9 = Button(cal, padx=16, bd=5, fg='white', font=('arial', 20),
              text="9", bg='grey', command=lambda: btnClick(9)).grid(row=1, column=2)
add_btn = Button(cal, padx=16, bd=5, fg='white', font=('arial', 20),
                 text="+", bg='grey', command=lambda: btnClick('+')).grid(row=1, column=3)
# =============================================================================
btn4 = Button(cal, padx=16, bd=5, fg='white', font=('arial', 20),
              text="4", bg='grey', command=lambda: btnClick(4)).grid(row=2, column=0)
btn5 = Button(cal, padx=16, bd=5, fg='white', font=('arial', 20),
              text="5", bg='grey', command=lambda: btnClick(5)).grid(row=2, column=1)
btn6 = Button(cal, padx=16, bd=5, fg='white', font=('arial', 20),
              text="6", bg='grey', command=lambda: btnClick(6)).grid(row=2, column=2)
sub_btn = Button(cal, padx=16, bd=5, fg='white', font=('arial', 20),
                 text="-", bg='grey', command=lambda: btnClick('-')).grid(row=2, column=3)
# =============================================================================
btn1 = Button(cal, padx=16, bd=5, fg='white', font=('arial', 20),
              text="1", bg='grey', command=lambda: btnClick(1)).grid(row=3, column=0)
btn2 = Button(cal, padx=16, bd=5, fg='white', font=('arial', 20),
              text="2", bg='grey', command=lambda: btnClick(2)).grid(row=3, column=1)
btn3 = Button(cal, padx=16, bd=5, fg='white', font=('arial', 20),
              text="3", bg='grey', command=lambda: btnClick(3)).grid(row=3, column=2)
mult_btn = Button(cal, padx=16, bd=5, fg='white', font=('arial', 20),
                  text="*", bg='grey', command=lambda: btnClick('*')).grid(row=3, column=3)
# =============================================================================
btn0 = Button(cal, padx=16, bd=5, fg='white', font=('arial', 20),
              text="0", bg='grey', command=lambda: btnClick(0)).grid(row=4, column=1)
clear_btn = Button(cal, padx=16, bd=5, fg='white', font=('arial', 20),
                   text="C", bg='grey', command=lambda: btnClearDisplay()).grid(row=4, column=0)
equal_btn = Button(cal, padx=16, bd=5, fg='white', font=('arial', 20),
                   text="=", bg='grey', command=btnEqualsInput).grid(row=4, column=2)
div_btn = Button(cal, padx=16, bd=5, fg='white', font=('arial', 20),
                 text="/", bg='grey', command=lambda: btnClick('/')).grid(row=4, column=3)
# =============================================================================
cal.mainloop()