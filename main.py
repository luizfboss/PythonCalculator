from tkinter import *


# Button click
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)


# Clear button
def btnClearDisplay():
    global operator
    operator = ''
    text_input.set('')


# Equal Button
def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)


# Creation of the Calculator's 'body'
cal = Tk()
cal.title('Calculator')
operator = ''
text_input = StringVar()

# Calculator's Text Display
txtDisplay = Entry(cal, textvariable=text_input, bd=30, insertwidth=4,
                   bg='grey', justify='right').grid(columnspan=4)
# =============================================================================
# Before going to the code, it is important for you to understand the parameters in each button:
# padx - Padding of the button
# bd - Button size
# fg - Font Color
# font - Text Font and Size
# text - The Text Shown On The Button
# bg - Background Color
# command - the execution once that button is clicked
# =============================================================================
# Button 7, 8, 9, Sum - First row
btn7 = Button(cal, padx=16, bd=5, fg='white', font=('arial', 20),
              text="7", bg='grey', command=lambda: btnClick(7)).grid(row=1, column=0)
btn8 = Button(cal, padx=16, bd=5, fg='white', font=('arial', 20),
              text="8", bg='grey', command=lambda: btnClick(8)).grid(row=1, column=1)
btn9 = Button(cal, padx=16, bd=5, fg='white', font=('arial', 20),
              text="9", bg='grey', command=lambda: btnClick(9)).grid(row=1, column=2)
add_btn = Button(cal, padx=16, bd=5, fg='white', font=('arial', 20),
                 text="+", bg='grey', command=lambda: btnClick('+')).grid(row=1, column=3)
# =============================================================================
# Button 4, 5, 6, Subtract - Second row
btn4 = Button(cal, padx=16, bd=5, fg='white', font=('arial', 20),
              text="4", bg='grey', command=lambda: btnClick(4)).grid(row=2, column=0)
btn5 = Button(cal, padx=16, bd=5, fg='white', font=('arial', 20),
              text="5", bg='grey', command=lambda: btnClick(5)).grid(row=2, column=1)
btn6 = Button(cal, padx=16, bd=5, fg='white', font=('arial', 20),
              text="6", bg='grey', command=lambda: btnClick(6)).grid(row=2, column=2)
sub_btn = Button(cal, padx=16, bd=5, fg='white', font=('arial', 20),
                 text="-", bg='grey', command=lambda: btnClick('-')).grid(row=2, column=3)
# =============================================================================
# Button 1, 2, 3, Multiply - Third row
btn1 = Button(cal, padx=16, bd=5, fg='white', font=('arial', 20),
              text="1", bg='grey', command=lambda: btnClick(1)).grid(row=3, column=0)
btn2 = Button(cal, padx=16, bd=5, fg='white', font=('arial', 20),
              text="2", bg='grey', command=lambda: btnClick(2)).grid(row=3, column=1)
btn3 = Button(cal, padx=16, bd=5, fg='white', font=('arial', 20),
              text="3", bg='grey', command=lambda: btnClick(3)).grid(row=3, column=2)
mult_btn = Button(cal, padx=16, bd=5, fg='white', font=('arial', 20),
                  text="*", bg='grey', command=lambda: btnClick('*')).grid(row=3, column=3)
# =============================================================================
# Button 0, Clear, Equal, Divide - Last row
btn0 = Button(cal, padx=16, bd=5, fg='white', font=('arial', 20),
              text="0", bg='grey', command=lambda: btnClick(0)).grid(row=4, column=1)
clear_btn = Button(cal, padx=16, bd=5, fg='white', font=('arial', 20),
                   text="C", bg='grey', command=lambda: btnClearDisplay()).grid(row=4, column=0)
equal_btn = Button(cal, padx=16, bd=5, fg='white', font=('arial', 20),
                   text="=", bg='grey', command=btnEqualsInput).grid(row=4, column=2)
div_btn = Button(cal, padx=16, bd=5, fg='white', font=('arial', 20),
                 text="/", bg='grey', command=lambda: btnClick('/')).grid(row=4, column=3)
# ============================================================================
# Execute the code in a loop that won't close except the user closes the calculator's tab
cal.mainloop()
