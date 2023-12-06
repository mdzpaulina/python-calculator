import tkinter 
from tkinter import *
import os
from PIL import ImageTk, Image

carpeta_principal = os.path.dirname(__file__)
carpeta_imagenes = os.path.join(carpeta_principal, "imagenes")

root = Tk()
root.title("Calculadora simple")
root.iconbitmap(os.path.join(carpeta_imagenes, "calculator.ico"))
root.geometry("340x520")
root.resizable(False, False)
root.configure(bg="#17161b")

equation = ""

def show(value):
    global equation
    equation+= value
    label_result.config(text = equation)
def clear():
    global equation
    equation = ""
    label_result.config(text = equation)
    
def calculate():
    global equation
    result=""
    if equation !="":
        try:
            result= eval(equation)
        except:
            result="error"
            equation = ""
    label_result.config(text=result)
    

label_result = Label(root, width=25, height= 3, text= "", font=("arial",20), fg="#fff", bg= "#2a2d36")
label_result.pack()

Button(root,text="CE", width= 3, height= 1, font =("arial", 30, "bold"), bd=1, fg="#fff", bg= "#3697f5", command= lambda: clear()).place(x=2, y= 100)
Button(root,text="%", width= 3, height= 1, font =("arial", 30, "bold"), bd=1, fg="#fff", bg= "#2a2d36",command = lambda: show("%")).place(x=87, y= 100)
Button(root,text="+", width= 3, height= 1, font =("arial", 30, "bold"), bd=1, fg="#fff", bg= "#2a2d36",command = lambda: show("+")).place(x=172, y= 100)
Button(root,text="-", width= 3, height= 1, font =("arial", 30, "bold"), bd=1, fg="#fff", bg= "#2a2d36",command = lambda: show("-")).place(x=257, y= 100)

Button(root,text="7", width= 3, height= 1, font =("arial", 30, "bold"), bd=1, fg="#fff", bg= "#2a2d36",command = lambda: show("7")).place(x=2, y= 184)
Button(root,text="8", width= 3, height= 1, font =("arial", 30, "bold"), bd=1, fg="#fff", bg= "#2a2d36",command = lambda: show("8")).place(x=87, y= 184)
Button(root,text="9", width= 3, height= 1, font =("arial", 30, "bold"), bd=1, fg="#fff", bg= "#2a2d36",command = lambda: show("9")).place(x=172, y= 184)
Button(root,text="÷", width= 3, height= 1, font =("arial", 30, "bold"), bd=1, fg="#fff", bg= "#2a2d36",command = lambda: show("/")).place(x=257, y= 184)

Button(root,text="4", width= 3, height= 1, font =("arial", 30, "bold"), bd=1, fg="#fff", bg= "#2a2d36",command = lambda: show("4")).place(x=2, y= 268)
Button(root,text="5", width= 3, height= 1, font =("arial", 30, "bold"), bd=1, fg="#fff", bg= "#2a2d36",command = lambda: show("5")).place(x=87, y= 268)
Button(root,text="6", width= 3, height= 1, font =("arial", 30, "bold"), bd=1, fg="#fff", bg= "#2a2d36",command = lambda: show("6")).place(x=172, y= 268)
Button(root,text="x", width= 3, height= 1, font =("arial", 30, "bold"), bd=1, fg="#fff", bg= "#2a2d36",command = lambda: show("*")).place(x=257, y= 268)

Button(root,text="1", width= 3, height= 1, font =("arial", 30, "bold"), bd=1, fg="#fff", bg= "#2a2d36",command = lambda: show("1")).place(x=2, y= 352)
Button(root,text="2", width= 3, height= 1, font =("arial", 30, "bold"), bd=1, fg="#fff", bg= "#2a2d36",command = lambda: show("2")).place(x=87, y= 352)
Button(root,text="3", width= 3, height= 1, font =("arial", 30, "bold"), bd=1, fg="#fff", bg= "#2a2d36",command = lambda: show("3")).place(x=172, y= 352)
Button(root,text="=", width= 3, height= 3, font =("arial", 30, "bold"), bd=1, fg="#fff", bg= "#fe9037",command= lambda:calculate()).place(x=257, y= 352)

Button(root,text="0", width= 7, height= 1, font =("arial", 30, "bold"), bd=1, fg="#fff", bg= "#2a2d36",command = lambda: show("0")).place(x=0, y= 436)
Button(root,text=".", width= 3, height= 1, font =("arial", 30, "bold"), bd=1, fg="#fff", bg= "#2a2d36",command = lambda: show(".")).place(x=172, y= 436)


root.mainloop()