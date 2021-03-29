import sympy as sp
from sympy.solvers import solveset
from sympy import Symbol
from sympy import var
from sympy import sympify
from sympy import Eq
import math
from sympy import *
import tkinter as tk
import numpy as np

def FindMainVar(equation):
    i=0
    for x in eq:
        if eq[i]>='x' and eq[i]<='z':
            MainVar=eq[i]
            break
        i=i+1
    return MainVar

def MakeStringReady(equation):
    ParsableEq=''
    i=0
    for x in equation:
        if equation[i]=='=':
            break
        elif equation[i]=='^':
            ParsableEq=ParsableEq+"**"
        elif (equation[i]>='0' and equation[i]<='9') and (equation[i+1]>='a' and equation[i+1]<='z'):
            ParsableEq=ParsableEq+equation[i]
            ParsableEq=ParsableEq+'*'
        else:         
            ParsableEq=ParsableEq+equation[i]
        
        i=i+1
    return ParsableEq

def Bisection(equation,MainVar):
    tolerance=float(input("Enter the tolerance value = "))
    a=float(input("Enter the value of 'a' = "))
    b=float(input("Enter the value of 'b' = "))

    decider=equation.evalf(subs={MainVar:a})
    decider=float(decider)
    if decider<0:
        negative=a
        positive=b
    else: 
        positive=a
        negative=b
    AbsoluteError=0
    CheckFlag=0
    prevc=0
    i=1
    while (AbsoluteError>tolerance or CheckFlag==0):
        PosinFunc=float(equation.evalf(subs={MainVar:positive}))
        NeginFunc=float(equation.evalf(subs={MainVar:negative}))
        if PosinFunc*NeginFunc>0:
            print("IVT failed , aborting iterations ")
            break
        c=(negative+positive)/2
        AbsoluteError=math.fabs(c-prevc)
        print(str(i)+'.) '+str(c)+"                                                                                      "+str(AbsoluteError))
        if AbsoluteError<tolerance:
            break
        
        CheckFlag=CheckFlag+1
        CinFunc=float(equation.evalf(subs={MainVar:c}))
        if CinFunc<0:
            negative=c
        else :
            positive=c
        prevc=c
        i=i+1
    print("A suitable root within the given tolerance value is = "+str(c))

def RegularFalsi(equation,MainVar):
    tolerance=float(input("Enter the tolerance value = "))
    a=float(input("Enter the value of 'a' = "))
    b=float(input("Enter the value of 'b' = "))

    decider=equation.evalf(subs={MainVar:a})
    decider=float(decider)
    if decider<0:
        negative=a
        positive=b
        A_Status='Negative'
    else: 
        positive=a
        negative=b
        A_Status='Positive'
    AbsoluteError=0
    CheckFlag=0
    prevc=0
    i=1
    while (AbsoluteError>tolerance or CheckFlag==0):
          PosInFunc=float(equation.evalf(subs={MainVar:positive}))
          NegInFunc=float(equation.evalf(subs={MainVar:negative}))
          if (PosInFunc*NegInFunc>0):
              print("IVT failed, aborting iterations ")
              break
          c=(a*float(equation.evalf(subs={MainVar:b}))-b*float(equation.evalf(subs={MainVar:a})))
          c=c/(float(equation.evalf(subs={MainVar:b}))-float(equation.evalf(subs={MainVar:a})))
          AbsoluteError=math.fabs(c-prevc)
          print(str(i)+'.) '+str(c)+"                                                                              "+str(AbsoluteError))
          if AbsoluteError<tolerance:
            break
          CinFunc=float(equation.evalf(subs={MainVar:c}))
          if (CinFunc<0):
              if (A_Status=='Positive'):
                  b=c 
              else:
                  a=c 
          else :
              if(A_Status=='Positive'):
                  a=c
              else:
                  b=c            
          prevc=c
          i=i+1
    print("A suitable root within the given tolerance value is = "+str(c))     

def Secant(equation,MainVar):
      tolerance=float(input("Enter the tolerance value = "))
      a=float(input("Enter the value of 'a' = "))
      b=float(input("Enter the value of 'b' = "))
      AbsoluteError=0
      CheckFlag=0
      prevc=0
      i=1
      while(AbsoluteError>tolerance or CheckFlag==0):
          c=(a*float(equation.evalf(subs={MainVar:b}))-b*float(equation.evalf(subs={MainVar:a})))
          c=c/(float(equation.evalf(subs={MainVar:b}))-float(equation.evalf(subs={MainVar:a})))
          AbsoluteError=math.fabs(c-prevc)
          print(str(i)+'.) '+str(c)+"                                                                              "+str(AbsoluteError))
          a=b
          b=c 
          i=i+1
          if(AbsoluteError<tolerance):
              break
          prevc=c 
      print("A suitable root within the given tolerance value is = "+str(c))      

def NewtonRaphson(equation,MainVar):
      tolerance=float(input("Enter the tolerance value = "))
      a=float(input("Enter the value of 'a' = "))
      b=float(input("Enter the value of 'b' = "))
      AbsoluteError=0
      CheckFlag=0
      PrevP=0
      i=1
      p=float(a+b/2)
      while(AbsoluteError>tolerance or CheckFlag==0):
          PInFunc=float(equation.evalf(subs={MainVar:p}))
          DerEq=diff(equation,MainVar)
          PInDer=float(DerEq.evalf(subs={MainVar:p}))
          PNext=float(p-(PInFunc/PInDer))
          AbsoluteError=math.fabs(PNext-PrevP)
          print(str(i)+'.) '+str(PNext)+"                                                                              "+str(AbsoluteError))
          if(AbsoluteError<tolerance):
              break
          i=i+1
          PrevP=PNext
          p=PNext 
      print("A sutibale root within the given tolerance value is = "+str(PNext))           

def FixedPointIteration(equation,MainVar):
      tolerance=float(input("Enter the tolerance value = "))
      a=float(input("Enter the value of 'a' = "))
      b=float(input("Enter the value of 'b' = "))
      while(1):
          NormalEq=input("Enter g(x), press QUIT if you want to terminate here : ")
          if(NormalEq=='QUIT'):
              break
          ReadyEq=MakeStringReady(NormalEq)
          ReadyEq=sympify(ReadyEq)
          AbsoluteError=0
          CheckFlag=0
          PrevP=0
          i=1
          p=a
          CummulativeAbsError=0
          while(AbsoluteError>tolerance or CheckFlag==0):
              PInFunc=float(ReadyEq.evalf(subs={MainVar:p}))
              AbsoluteError=math.fabs(PInFunc-PrevP)
              print(str(i)+'.) '+str(PInFunc)+"                                                                              "+str(AbsoluteError))
              if(AbsoluteError<tolerance):
                print("A sutibale root within the given tolerance value is = "+str(PInFunc))
                break
              i=i+1
              PrevP=PInFunc
              CummulativeAbsError=math.fabs(AbsoluteError+AbsoluteError)
              if(CummulativeAbsError>20):
                  print("The function is divergent so a solution wont exist here ")
                  break
              p=PInFunc

def LagrangeInterpolation():
    n=int(input("Enter the total number of data points : "))
    x=np.zeros(n,dtype=float)
    y=np.zeros(n,dtype=float)
    i=0
    while i!=n:
        x[i]=float(input("Enter the value of x"+str(i)+" : "))
        i=i+1
    InterPol=float(input("Enter the interpolation value : "))
    eq=input("Enter the equation (Press QUIT to directly input y values): ")
    if eq!="QUIT":
        ReadyEq=MakeStringReady(eq)
        MainVar=FindMainVar(eq)
        MainVar=symbols(MainVar)
        ReadyEq=sympify(ReadyEq)
        i=0
        while i!=n:
            y[i]=float(ReadyEq.evalf(subs={MainVar:x[i]}))
            i=i+1
    else:
        i=0
        while i!=n:
            y[i]=float(input("Enter the value of y"+str(i)+" : "))
            i=i+1

    result=0
    for i in range(n):
        temp=1
        for j in range(n):
            if i!=j:
                temp=temp*(InterPol-x[j])/(x[i]-x[j])
        result=result+(temp*y[i])
    print("The result of interpolation is = "+str(result))



MainWindow=tk.Tk()
eq=input("Enter the equation :")

i=0
for x in eq:
    if eq[i]>='x' and eq[i]<='z':
        MainVar=eq[i]
        break
    i=i+1

print(MainVar)
NewVar=symbols(MainVar)
NewStr=MakeStringReady(eq)
NewStr=sympify(NewStr)
LagrangeInterpolation()
#FixedPointIteration(NewStr,MainVar)
NewtonRaphson(NewStr,MainVar)
Secant(NewStr,MainVar)
RegularFalsi(NewStr,MainVar)
Bisection(NewStr,MainVar)
i=0
MainWindow.mainloop();