from tkinter import *
import calc
import math



next2=False

def click(key):
    if key=="=":
        try:
            result=str(eval(display.get()))
            display.insert(END,"="+result)
        except ZeroDivisionError as msg:
            display.insert(END,"-->ZeroDivisionError! : %s !"%(str(msg).capitalize()))
    elif key=="C":
        display.delete('0',END)
    elif key==constant_list[0]:
        display.insert(END,math.pi)
    elif key==constant_list[1]:
        display.insert(END,"299792458")
    elif key==constant_list[2]:
        display.insert(END,"340")
    elif key==constant_list[3]:
        display.insert(END,"149597887.5")
    elif key==constant_list[4]:
        display.insert(END,"6371")
    elif key==constant_list[5]:
        display.insert(END,"384403")
    elif key==constant_list[6]:
        display.insert(END,math.e)
    elif key==functions_list[0]:
        n=display.get()
        display.delete('0',END)
        display.insert(END,"--->factorial(!)== ")
        display.insert(END,calc.fractional(n))
    elif key==functions_list[1]:
        n=display.get()
        display.delete('0',END)
        display.insert(END,"--->roman== ")
        display.insert(END,calc.roman(n))
    elif key==functions_list[2]:
        n=display.get()
        display.delete('0',END)
        display.insert(END,"--->binary== ")
        display.insert(END,calc.binary(n))
    elif key==functions_list[3]:
        n=display.get()
        display.delete('0',END)
        display.insert(END,"--->basic== ")
        display.insert(END,calc.basic(n))
    elif key==functions_list[4]:
        n=display.get()
        display.delete('0',END)
        display.insert(END,"--->x^x== ")
        display.insert(END,calc.kwadrat(n))
    elif key==functions_list[5]:
        n=display.get()
        display.delete('0',END)
        display.insert(END,"--->x^(-x)== ")
        display.insert(END,calc.kwadrat2(n))
    elif key==functions_list[6]:
        n=display.get()
        display.delete('0',END)
        display.insert(END,"--->sqrt== ")
        display.insert(END,calc.sqrt(n))
    elif key==functions_list[7]:
        n=display.get()
        display.delete('0',END)
        display.insert(END,"--->tan== ")
        display.insert(END,calc.tan(n))
    elif key==functions_list[8]:
        n=display.get()
        display.delete('0',END)
        display.insert(END,"--->sin==")
        display.insert(END,calc.sin(n))
    elif key==functions_list[9]:
        n=display.get()
        display.delete('0',END)
        display.insert(END,"--->cos== ")
        display.insert(END,calc.cos(n))
    else:
        display.insert(END,key)

window1=Tk()
window1.title("Calculator")
window1.resizable(0,0)

window=Frame(window1,bg="navy")
window.grid()

top_row=Frame(window)
top_row.grid(row=0,column=0,columnspan=2,sticky=N)

display=Entry(top_row,width=45,bg="navy",fg='aqua')
display.grid()

num_pad=Frame(window)
num_pad.grid(row=1,column=0,sticky=W)

num_list=[
    '7','8','9',
    '4','5','6',
    '1','2','3',
    '0','.','=']

r=0
c=0
for btn_text in num_list:
    def cmd(x=btn_text):
        click(x)
    Button(num_pad,text=btn_text,width=5,command=cmd,bg='aqua',fg='blue',activeforeground='blue',activebackground='aqua').grid(row=r,column=c)
    c=c+1
    if c>2:
        c=0
        r=r+1

operator=Frame(window,bg='navy')
operator.grid(row=1,column=1,sticky=W)

operator_list=[
    '*','/',
    '+','-',
    '(',')',
    'C']

r=0
c=0
for btn_text in operator_list:
    def cmd(x=btn_text):
        click(x)
    Button(operator,text=btn_text,width=5,command=cmd,bg='aqua',fg='blue',activeforeground='blue',activebackground='aqua').grid(row=r,column=c)
    c=c+1
    if c>1:
        c=0
        r=r+1

constant=Frame(window,bg='aqua')
constant.grid(row=3,column=0,sticky=W)

constant_list=[
    'pi',
    'speed of light (m/s)',
    'speed of sound (m/s)',
    'avg dist to sun (km)',
    'avg dist to moon (km)',
    'Earth radius (km)',
    'e']
    

r=0
c=0
for btn_text in constant_list:
    def cmd(x=btn_text):
        click(x)
    Button(constant,text=btn_text,width=22,command=cmd,bg='aqua',fg='blue',activeforeground='blue',activebackground='aqua').grid(row=r,column=c)
    r=r+1

functions=Frame(window,bg='aqua')
functions.grid(row=3,column=1,sticky=W)

functions_list=[
    'factorial (!)',
    '-> roman',
    '-> binary',
    'binary -> 10',
    'x^x',
    'x^(-x)',
    'sqrt',
    'tan',
    'sin',
    'cos']

r=0
c=0
for btn_text in functions_list:
    def cmd(x=btn_text):
        click(x)
    Button(functions,text=btn_text,width=13,command=cmd,bg='aqua',fg='blue',activeforeground='blue',activebackground='aqua').grid(row=r,column=c)
    r=r+1

window.mainloop()

