from tkinter import *
gui = Tk() 
gui.configure(background="light green") 
gui.title("Simple Calculator")
gui.geometry("270x150") 

def btn_clk(a):
    global expression
    expression = expression + str(a)  
    equation.set(expression) 
    

def equal():
    global expression
    result = str(eval(expression)) 
    equation.set(result)
    expression = ""

def clr():
    global expression
    expression = ""
    equation.set("")

expression=""
equation = StringVar()

# create the text entry box for 
# showing the expression . 
expression_field = Entry(gui, textvariable=equation)
expression_field.grid(columnspan=4, ipadx=70)
 

button1 = Button(gui, text=' 1 ', fg='black',command=lambda n1="1":btn_clk(n1),bg='grey', height=1, width=7) 
button1.grid(row=2, column=0) 

button2 = Button(gui, text=' 2 ', fg='black',command=lambda n1="2":btn_clk(n1) ,bg='grey',height=1, width=7) 
button2.grid(row=2, column=1) 

button3 = Button(gui, text=' 3 ', fg='black',command=lambda n1="3":btn_clk(n1), bg='grey', height=1, width=7) 
button3.grid(row=2, column=2) 

button4 = Button(gui, text=' 4 ', fg='black',command=lambda n1="4":btn_clk(n1), bg='grey', height=1, width=7)
button4.grid(row=3, column=0)

button5 = Button(gui, text=' 5 ', fg='black',command=lambda n1="5":btn_clk(n1),bg='grey', height=1, width=7) 
button5.grid(row=3, column=1) 

button6 = Button(gui, text=' 6 ', fg='black',command=lambda n1="6":btn_clk(n1), bg='grey', height=1, width=7) 
button6.grid(row=3, column=2) 

button7 = Button(gui, text=' 7 ', fg='black',command=lambda n1="7":btn_clk(n1), bg='grey',height=1, width=7) 
button7.grid(row=4, column=0) 

button8 = Button(gui, text=' 8 ', fg='black',command=lambda n1="8":btn_clk(n1), bg='grey',height=1, width=7) 
button8.grid(row=4, column=1) 

button9 = Button(gui, text=' 9 ', fg='black',command=lambda n1="9":btn_clk(n1), bg='grey', height=1, width=7) 
button9.grid(row=4, column=2) 

button0 = Button(gui, text=' 0 ', fg='black',command=lambda n1="0":btn_clk(n1), bg='grey', height=1, width=7) 
button0.grid(row=5, column=0) 

plus = Button(gui, text=' + ', fg='black',command=lambda n1="+":btn_clk(n1),bg='grey',height=1, width=7) 
plus.grid(row=2, column=3) 

minus = Button(gui, text=' - ', fg='black',command=lambda n1="-":btn_clk(n1), bg='grey', height=1, width=7) 
minus.grid(row=3, column=3) 

multiply = Button(gui, text=' * ', fg='black',command=lambda n1="*":btn_clk(n1), bg='grey', height=1, width=7) 
multiply.grid(row=4, column=3) 

divide = Button(gui, text=' / ', fg='black',command=lambda n1="/":btn_clk(n1), bg='grey', height=1, width=7) 
divide.grid(row=5, column=3) 

equal = Button(gui, text=' = ', fg='black',command=equal, bg='grey', height=1, width=7) 
equal.grid(row=5, column=2)

clear = Button(gui, text='Clear', fg='black',command=clr, bg='grey', height=1, width=7) 
clear.grid(row=5, column='1') 

Decimal= Button(gui, text='.', fg='black',command=lambda n1=".":btn_clk(n1), bg='grey', height=1, width=7) 
Decimal.grid(row=6, column=0) 

gui.mainloop() 

