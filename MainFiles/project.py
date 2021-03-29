#import sympy as sp
from sympy.solvers import solveset
from sympy import Symbol
from sympy import var
from sympy import sympify
from sympy import Eq
import math
from sympy import *
import tkinter as tk
from array import *

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
        elif equation[i] == 'e' and equation[i+1]=='^':
            ParsableEq=ParsableEq+"exp("
            i=i+2
            for x in equation:
                if (equation[i]>='0' and equation[i]<='9') and (equation[i+1]>='a' and equation[i+1]<='z'):
                    ParsableEq=ParsableEq+equation[i]
                    ParsableEq=ParsableEq+'*'
                elif equation[i]>='a' and equation[i]<='z':
                    ParsableEq=ParsableEq+equation[i]
                else:
                    break
                i=i+1
            ParsableEq=ParsableEq+')'
            i=i-1
        else:         
            ParsableEq=ParsableEq+equation[i]
        i=i+1
    return ParsableEq

def Bisection(equation,MainVar):
    global a
    global b
    decider=equation.evalf(subs={MainVar:a}) #substitute a as value of mainvar. then evaluate and give value to decider
    decider=float(decider)
    if decider<0:
        negative=a
        positive=b
    else: 
        positive=a
        negative=b
    AbsoluteError=1
    prevc=0
    i=1
    while (AbsoluteError>tolerance):
        PosinFunc=float(equation.evalf(subs={MainVar:positive}))
        NeginFunc=float(equation.evalf(subs={MainVar:negative}))
        if PosinFunc*NeginFunc>0:
            print("IVT failed , aborting iterations!")
            return 
        c=(negative+positive)/2
        AbsoluteError=math.fabs(c-prevc)
        print(str(i)+'.) '+str(c)+"                                                                                      "+str(AbsoluteError))
        if AbsoluteError<tolerance:
            break
        
        CinFunc=float(equation.evalf(subs={MainVar:c}))
        if CinFunc<0:
            negative=c
        else :
            positive=c
        prevc=c
        i=i+1
    print("A suitable root within the given tolerance value is = "+str(c))

def RegularFalsi(equation,MainVar):
    # tolerance=float(input("Enter the tolerance value = "))
    # a=float(input("Enter the value of 'a' = "))
    # b=float(input("Enter the value of 'b' = "))
    global a
    global b
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
    AbsoluteError=1
    prevc=0
    i=1
    while (AbsoluteError>tolerance):
          PosInFunc=float(equation.evalf(subs={MainVar:positive}))
          NegInFunc=float(equation.evalf(subs={MainVar:negative}))
          if (PosInFunc*NegInFunc>0):
              print("IVT failed, aborting iterations ")
              return
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
    #   tolerance=float(input("Enter the tolerance value = "))
    #   a=float(input("Enter the value of 'a' = "))
    #   b=float(input("Enter the value of 'b' = "))
    global a
    global b
    AbsoluteError=1
    prevc=0
    i=1
    while(AbsoluteError>tolerance):
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
    #   tolerance=float(input("Enter the tolerance value = "))
    #   a=float(input("Enter the value of 'a' = "))
    #   b=float(input("Enter the value of 'b' = "))
    global a
    global b
    AbsoluteError=1
    PrevP=0
    i=1
    p=float(a+b/2)
    while(AbsoluteError>tolerance):
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
    #   tolerance=float(input("Enter the tolerance value = "))
    #   a=float(input("Enter the value of 'a' = "))
    #   b=float(input("Enter the value of 'b' = "))
    #print("Fixed Point is working under the assumption that you have entered a function G(x) instead of the original F(x)!")

    # NormalEq=input("Enter g(x), press QUIT if you want to terminate here : ")
    # if(NormalEq=='QUIT'):
    #     return
    # ReadyEq=MakeStringReady(NormalEq)
    # ReadyEq=sympify(ReadyEq)
    ReadyEq=equation
    AbsoluteError=1
    PrevP=0
    i=1
    p=a
    errors = array('d',[a,a,a,a,a])
    #CummulativeAbsError=0
    while(AbsoluteError>tolerance):
        PInFunc=float(ReadyEq.evalf(subs={MainVar:p}))
        AbsoluteError=math.fabs(PInFunc-PrevP)
        print(str(i)+'.) '+str(PInFunc)+"                                                                              "+str(AbsoluteError))
        errors.append(AbsoluteError)
        errors.pop(0)
        if(AbsoluteError<tolerance):
            print("A sutibale root within the given tolerance value is = "+str(PInFunc))
            break
        elif errors[4]==errors[2]:
            print("The function entered in bouncing between two values and is not convergent!")
            break
        elif (math.fabs(errors[4]-errors[3]) > math.fabs(errors[3]-errors[2])) and (math.fabs(errors[3]-errors[2]) > math.fabs(errors[2]-errors[1])) and math.fabs((errors[2]-errors[1]) > math.fabs(errors[1]-errors[0])):
            print("The function enetered is divergent!")
            break
        elif i>300:
            print("The function did not reach the tolerance value after 300 iterations! Stopping calculation...")
            break
        i=i+1
        PrevP=PInFunc
        #CummulativeAbsError=math.fabs(AbsoluteError+AbsoluteError)
        # if(CummulativeAbsError>20):
        #     print("The function is divergent so a solution wont exist here ")
        #     break
        p=PInFunc


#MainWindow=tk.Tk()
eq=input("Enter the equation :")
tolerance=float(input("Enter the tolerance value = "))
a=float(input("Enter the value of 'a' = "))
b=float(input("Enter the value of 'b' = "))

i=0
for x in eq:
    if eq[i]>='x' and eq[i]<='z':
        MainVar=eq[i]
        break
    i=i+1

print("The variable has been recognized as: " + MainVar)
NewVar=symbols(MainVar) #Creates a sympy symbol named NewVar
NewStr=MakeStringReady(eq)
NewStr=sympify(NewStr)  #makes a sympy expression/equation
FixedPointIteration(NewStr,MainVar)
# Bisection(NewStr,MainVar)
# RegularFalsi(NewStr,MainVar)
# NewtonRaphson(NewStr,MainVar)
# Secant(NewStr,MainVar)
i=0
# while i!=5:
#     TempStr=NewStr
#     print("The value of "+eq+" At x = "+ str(i) +" is:")
#     NewStr=sympify(NewStr)
#     print(NewStr.evalf(subs={MainVar:i}))
#     print('\n')
#     i=i+1

#MainWindow.mainloop();