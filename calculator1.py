import tkinter
from tkinter import *
# create a window
root=Tk()
root.title("Calculator")
root.geometry("400x400+50+50")
root.resizable(False,False)
root.configure(bg="black")
# creating a label to display the calculator input/output
l=Label(root,width=20,height=1,text="",font=("arial",30))
l.pack()

# creating buttons for the calculator
Button(root,text="C",width=16,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="blue",command=lambda: clear()).place(x=10,y=60)
Button(root,text="/",width=5,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="orange",command=lambda: show("/")).place(x=300,y=60)

Button(root,text="7",width=5,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda: show("7")).place(x=10,y=120)
Button(root,text="8",width=5,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda: show("8")).place(x=105,y=120)
Button(root,text="9",width=5,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda: show("9")).place(x=200,y=120)
Button(root,text="*",width=5,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="orange",command=lambda: show("*")).place(x=300,y=120)

Button(root,text="4",width=5,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda: show("4")).place(x=10,y=180)
Button(root,text="5",width=5,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda: show("5")).place(x=105,y=180)
Button(root,text="6",width=5,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda: show("6")).place(x=200,y=180)
Button(root,text="-",width=5,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="orange",command=lambda: show("-")).place(x=300,y=180)

Button(root,text="1",width=5,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda: show("1")).place(x=10,y=240)
Button(root,text="2",width=5,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda: show("2")).place(x=105,y=240)
Button(root,text="3",width=5,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda: show("3")).place(x=200,y=240)
Button(root,text="+",width=5,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="orange",command=lambda: show("+")).place(x=300,y=240)


Button(root,text="0",width=10,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda: show("0")).place(x=10,y=300)
Button(root,text=".",width=5,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="blue",command=lambda: show(".")).place(x=200,y=300)
Button(root,text="=",width=5,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="orange",command=lambda: cal()).place(x=300,y=300)
# intialize the exp variable
exp=""
# Defining functions for calculator operations
def show(val):
    # Updates the expression when a button is clicked
    global exp
    exp+=val
    l.config(text=exp)
    
def clear():
    # Clears the expression
    global exp
    exp=""
    l.config(text=exp)
    
def cal():
    # TO Evaluate and display the result
    global exp
    res=""
    if exp !="":
        try:
            res=eval(exp)
        except:
            res="Invalid"
            exp = ""
    l.config(text=res)

# start of main loop
root.mainloop()
