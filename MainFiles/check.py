import sympy as sp
from sympy.solvers import solveset
from sympy import Symbol
from sympy import var
from sympy import sympify
from sympy import Eq
from tkinter import *
from tkinter import ttk
import math
from sympy import *

print(math.floor(0.5))
def switch():
    Tabs.select(SecondTab)

MainWindow=Tk()
exp="x+2*y"
exp=sympify(exp)
x=symbols('x')
y=symbols('y')
print(float(exp.evalf(subs={x:4,y:1})))
MainWindow.geometry("500x500")
MainWindow.title("Zephyr-I")
style=ttk.Style()
style.layout("TNotebook.Tab",[]) #hides the tab window 
Tabs=ttk.Notebook(MainWindow)
Tabs.pack()
FirstTab=Frame(Tabs,width=500,height=500,bg="black")
SecondTab=Frame(Tabs,width=500,height=500,bg="red")
# FirstTab.pack(fill="both",expand=1)
# SecondTab.pack(fill="both",expand=1)
Tabs.add(FirstTab, text="FirstTab") #adds the tab to the tab control 
Tabs.add(SecondTab,text="SecondTab")
TheButton=Button(FirstTab,text="Switch Tabs",command=switch).pack(pady=10)
MainWindow.mainloop()

x=symbols('x')
exp=ln(x-1)
c=(diff(exp,x))
print(str(c))