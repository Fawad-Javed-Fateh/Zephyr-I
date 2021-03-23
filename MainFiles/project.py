import sympy as sp
from sympy.solvers import solveset
from sympy import Symbol
from sympy import var
from sympy import sympify
from sympy import Eq
import math
from sympy import *

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
    while (AbsoluteError>tolerance or CheckFlag==0):
        PosinFunc=float(equation.evalf(subs={MainVar:positive}))
        NeginFunc=float(equation.evalf(subs={MainVar:negative}))
        if PosinFunc*NeginFunc>0:
            print("IVT failed , aborting iterations ")
            break
        c=(negative+positive)/2
        AbsoluteError=math.fabs(c-prevc)
        print(str(c)+"                                                                              "+str(AbsoluteError))
        if AbsoluteError<tolerance:
            break
        
        CheckFlag=CheckFlag+1
        CinFunc=float(equation.evalf(subs={MainVar:c}))
        if CinFunc<0:
            negative=c
        else :
            positive=c
        prevc=c
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
    while (AbsoluteError>tolerance or CheckFlag==0):
          PosInFunc=float(equation.evalf(subs={MainVar:positive}))
          NegInFunc=float(equation.evalf(subs={MainVar:negative}))
          if (PosInFunc*NegInFunc>0):
              print("IVT failed, aborting iterations ")
              break
          c=(a*float(equation.evalf(subs={MainVar:b}))-b*float(equation.evalf(subs={MainVar:a})))
          c=c/(float(equation.evalf(subs={MainVar:b}))-float(equation.evalf(subs={MainVar:a})))
          AbsoluteError=math.fabs(c-prevc)
          print(str(c)+"                                                                              "+str(AbsoluteError))
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
    print("A suitable root within the given tolerance value is = "+str(c))       


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
RegularFalsi(NewStr,MainVar)
Bisection(NewStr,MainVar)
i=0
# while i!=5:
#     TempStr=NewStr
#     print("The value of "+eq+" At x = "+ str(i) +" is:")
#     NewStr=sympify(NewStr)
#     print(NewStr.evalf(subs={MainVar:i}))
#     print('\n')
#     i=i+1

