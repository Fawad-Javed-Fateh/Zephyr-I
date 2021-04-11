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
import numpy as np

def FindMainVar(equation):
    i=0
    for x in equation:
        if equation[i]>='x' and equation[i]<='z':
            MainVar=equation[i]
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
            
    for z in range(n+1):
        result=0
        if z!=0 and z!=1:
            k=0
            RangeShifterX=np.zeros(n,dtype=float)
            RangeShifterY=np.zeros(n,dtype=float)
            while(InterPol>x[k]):
                k=k+1
            index=k-1
            BackIndex=k-1
            # while(BackIndex>=0):
            #      RangeShifterX[BackIndex]=x[k]
            #      RangeShifterY[BackIndex]=y[k]
            #      BackIndex=BackIndex-1
            #      k=k-1
            RangeShifterX[0]=x[k-1]
            RangeShifterX[1]=x[k]
            RangeShifterY[0]=y[k-1]
            RangeShifterY[1]=y[k] 
            k=2
            ForwardIndex=k
            SortIndex=k
            for a in range(n):
                flag=0
                for u in range(n):
                    if(x[a]==RangeShifterX[u] and x[a]!=0):
                        flag=flag+1
                if flag==0:
                    RangeShifterX[ForwardIndex]=x[a]
                    RangeShifterY[ForwardIndex]=y[a]
                    ForwardIndex=ForwardIndex+1
                if ForwardIndex>=n:
                    break 
            while(SortIndex<n):
                Iterator=SortIndex+1
                while(Iterator<n):
                    if RangeShifterX[SortIndex]<RangeShifterX[Iterator]:
                        tempvarx=RangeShifterX[SortIndex]
                        RangeShifterX[SortIndex]=RangeShifterX[Iterator]
                        RangeShifterX[Iterator]=tempvarx
                        tempvary=RangeShifterY[SortIndex]
                        RangeShifterY[SortIndex]=RangeShifterY[Iterator]
                        RangeShifterY[Iterator]=tempvary
                    Iterator=Iterator+1
                SortIndex=SortIndex+1

            for i in range(z):
                temp=1
                for j in range(z):
                    if i!=j:                       
                        temp=temp*(InterPol-RangeShifterX[j])/(RangeShifterX[i]-RangeShifterX[j])
                result=result+(temp*RangeShifterY[i])
            print("The result of interpolation of degree " +str(z-1)+ " is = " +str(result))

def DividedDifference():
    n=int(input("Enter the total number of data points : "))
    Xpoints=np.zeros(n,dtype=float)
    #Ypoints=np.zeros(n,dtype=float)
    Ypoint = []
    i=0
    while i!=n:
        Xpoints[i]=float(input("Enter the value of X"+str(i)+" : "))
        i=i+1
    InterPol=float(input("Enter the interpolation value : "))
    eq=input("Enter the equation or enter 0 to enter the values of y directly: ")
    
    if eq!="0":
        ReadyEq=MakeStringReady(eq)
        MainVar=FindMainVar(eq)
        MainVar=symbols(MainVar)
        ReadyEq=sympify(ReadyEq)
        i=0
        while i!=n:
            Ypoint.append(float(ReadyEq.evalf(subs={MainVar:x[i]})))
            i=i+1
    else:
        i=0
        while i!=n:
            Ypoint.append(input("Enter the value of y"+str(i)+" : "))
            i=i+1
    i=0
    Ypoints = []
    Ypoints.append(Ypoint)
    while i<(n-1):
        j=0
        y=[None]*(n-i-1)
        while j<(n-i-1):
            y[j]= (float(Ypoints[i][j+1])-float(Ypoints[i][j]))/(float(Xpoints[j+i+1])-float(Xpoints[j]))
            j=j+1
        Ypoints.append(y)
        i=i+1

    Answer=0
    Diff=0
    i=0
    while i<n:
        j=0
        Aval=float(Ypoints[i][0])
        while j<i:
            Diff=InterPol-Xpoints[j]
            Aval=Aval*Diff
            j=j+1
        Answer=Answer+Aval
        i=i+1
    print(str(Answer))

def ForwardDifference():
    n=int(input("Enter the total number of data points : "))
    Xpoints=np.zeros(n,dtype=float)
    #Ypoints=np.zeros(n,dtype=float)
    Ypoint = []
    height=0
    i=0
    while i!=n:
        Xpoints[i]=float(input("Enter the value of X"+str(i)+" : "))
        i=i+1
        if i==2:
            height = round(Xpoints[1]-Xpoints[0],5)
        elif i>2 and round((Xpoints[i-1]-Xpoints[i-2]),6)!=height:
            print("Equal spacing is required for Forward differnce!\n")
            return
    InterPol=float(input("Enter the interpolation value : "))
    eq=input("Enter the equation or enter 0 to enter the values of y directly: ")
    
    if eq!="0":
        ReadyEq=MakeStringReady(eq)
        MainVar=FindMainVar(eq)
        MainVar=symbols(MainVar)
        ReadyEq=sympify(ReadyEq)
        i=0
        while i!=n:
            Ypoint.append(float(ReadyEq.evalf(subs={MainVar:x[i]})))
            i=i+1
    else:
        i=0
        while i!=n:
            Ypoint.append(input("Enter the value of y"+str(i)+" : "))
            i=i+1
    f=Ypoint[0]
    Rounder=f[::-1].find('.')
    if Rounder<0:
        Rounder=0
    i=0
    Ypoints = []
    Ypoints.append(Ypoint)
    while i<(n-1):
        j=0
        y=[None]*(n-i-1)
        while j<(n-i-1):
            y[j]= round((float(Ypoints[i][j+1])-float(Ypoints[i][j]))/(float(Xpoints[j+i+1])-float(Xpoints[j])),Rounder)
            j=j+1
        Ypoints.append(y)
        i=i+1
    
    Var_S=round((InterPol-Xpoints[0])/height,Rounder)

    Answer=0
    Prod=0
    i=0
    while i<n:
        j=0
        Aval=float(Ypoints[i][0])
        Prod=1
        while j<i:
            k=0
            if j==0:
                Prod=Prod*(Var_S)
            if k<j:
                Prod=Prod*(Var_S-j)
            j=j+1
        Aval=Aval*Prod*height**i
        print(Aval)
        Answer=Answer+Aval
        i=i+1
    # print(str(Var_S))
    print(str(round(Answer,Rounder+1)))

def BackwardDifference():
    n=int(input("Enter the total number of data points : "))
    Xpoints=np.zeros(n,dtype=float)
    #Ypoints=np.zeros(n,dtype=float)
    Ypoint = []
    height=0
    i=0
    while i!=n:
        Xpoints[i]=float(input("Enter the value of X"+str(i)+" : "))
        i=i+1
        if i==2:
            height = round(Xpoints[1]-Xpoints[0],5)
        elif i>2 and round((Xpoints[i-1]-Xpoints[i-2]),6)!=height:
            print("Equal spacing is required for Backward differnce!\n")
            return
    InterPol=float(input("Enter the interpolation value : "))
    eq=input("Enter the equation or enter 0 to enter the values of y directly: ")
    
    if eq!="0":
        ReadyEq=MakeStringReady(eq)
        MainVar=FindMainVar(eq)
        MainVar=symbols(MainVar)
        ReadyEq=sympify(ReadyEq)
        i=0
        while i!=n:
            Ypoint.append(float(ReadyEq.evalf(subs={MainVar:x[i]})))
            i=i+1
    else:
        i=0
        while i!=n:
            Ypoint.append(input("Enter the value of y"+str(i)+" : "))
            i=i+1
    f=Ypoint[0]
    Rounder=f[::-1].find('.')
    if Rounder<0:
        Rounder=0
    i=0
    Ypoints = []
    Ypoints.append(Ypoint)
    while i<(n-1):
        j=0
        y=[None]*(n-i-1)
        while j<(n-i-1):
            y[j]= round((float(Ypoints[i][j+1])-float(Ypoints[i][j]))/(float(Xpoints[j+i+1])-float(Xpoints[j])),Rounder)
            j=j+1
        Ypoints.append(y)
        i=i+1
    
    Var_S=round((Xpoints[Xpoints.__len__()-1]-InterPol)/height,Rounder)

    Answer=0
    Prod=0
    i=0
    while i<n:
        j=0
        Aval=float(Ypoints[i][Ypoints[i].__len__() -1])
        Prod=1
        while j<i:
            k=0
            if j==0:
                Prod=Prod*(Var_S)
            if k<j:
                Prod=Prod*(Var_S+j)
            j=j+1
        Aval=Aval*Prod*height**i
        print(Aval)
        Answer=Answer+Aval
        i=i+1
    # print(str(Var_S))
    print(str(round(Answer,Rounder+1)))


def StirlingsMethod():
    #Rounder=f[::-1].find('.')
    n=int(input("Enter total number of data points "))
    x=np.zeros(n,dtype=float)
    y=np.zeros(n,dtype=float)
    SimpleDifferenceTable=np.zeros((n,n),dtype=float)
    print("Start entering x values, they must have equal spacing for simple difference ")
    for i in range(n):
        x[i]=input("Enter x"+str(i)+" = ")
    SimpleDifferenceTable[0][0]=0.23967
    SimpleDifferenceTable[1][0]=0.2806
    SimpleDifferenceTable[2][0]=0.31768
    SimpleDifferenceTable[3][0]=0.35204
    SimpleDifferenceTable[4][0]=0.36308

    # for i in range(n):
    #     SimpleDifferenceTable[i][0]=input("Enter y"+str(i)+" = ") 
    for i in range(1,n):
        for j in range(n-1):
            SimpleDifferenceTable[j][i]=SimpleDifferenceTable[j+1][i-1]-SimpleDifferenceTable[j][i-1]
    for i in range(n-1):
        for j in range(n-1):
            print(str(SimpleDifferenceTable[i][j])+" ")
        print("\n")
    InterPolVal=float(input("Enter the interpolation value "))
    diff=float(1)
    for i in range(n):
        if x[i]>InterPolVal:
            MidTerm=i-1
            p=float((-x[i-1]+InterPolVal)/diff)
            break
    if n==5:
        t1=float(SimpleDifferenceTable[MidTerm][0])
        t2=float(p*((SimpleDifferenceTable[MidTerm][1]+SimpleDifferenceTable[MidTerm-1][1])/2))
        t3=float(((p*p)/2)*SimpleDifferenceTable[MidTerm][2])
        t4p1=(p*p)*(p*p-1)/6
        t4=t4p1*((SimpleDifferenceTable[MidTerm][3]+SimpleDifferenceTable[MidTerm-1][3])/2)
        t5=float((p*p)*(p*p-1)/24)*(SimpleDifferenceTable[MidTerm][4])
        A=float(t1+t2+t3+t4+t5)
        A+round(A,4)
        print("The answers is = "+str(A))
        #t2=float(p*(SimpleDifferenceTable[]))        


def BackWardsSDT():
    n=int(input("Enter total number of data points "))
    x=np.zeros(n,dtype=float)
    y=np.zeros(n,dtype=float)
    SimpleDifferenceTable=np.zeros((n,n),dtype=float)
    print("Start entering x values, they must have equal spacing for simple difference ")
    for i in range(n):
        x[i]=input("Enter x"+str(i)+" = ")
    for i in range(n):
         SimpleDifferenceTable[i][0]=input("Enter y"+str(i)+" = ")
    for i in range(1,n):
        for j in range(n-i):
            SimpleDifferenceTable[j][i]=SimpleDifferenceTable[j+1][i-1]-SimpleDifferenceTable[j][i-1]
    
    InterPolVal=float(input("Enter the interpolation value : "))
    p= ((InterPolVal-x[n-1])/(x[1]-x[0]))
    permap=p
    j=n-2 
    ans = float(SimpleDifferenceTable[n-1][0])      
    for i in range(n-1):
        if i == 0:
            trp=SimpleDifferenceTable[j][i+1]
            ans = ans + (p*SimpleDifferenceTable[j][i+1])
            print(" At n = "+str(i)+" the value is = " + str(ans))
            j=j-1
        else :
            p=p*(permap+i)
            q=p
            trp=SimpleDifferenceTable[j][i+1]
            termer  = (q*(SimpleDifferenceTable[j][i+1])/math.factorial(i+1))
            ans = ans + (q*(SimpleDifferenceTable[j][i+1])/math.factorial(i+1))
            j=j-1    
            print(" At n = "+str(i)+" the value is = " + str(ans))

def ForWardsSDT():
    n=int(input("Enter total number of data points "))
    x=np.zeros(n,dtype=float)
    y=np.zeros(n,dtype=float)
    SimpleDifferenceTable=np.zeros((n,n),dtype=float)
    print("Start entering x values, they must have equal spacing for simple difference ")
    for i in range(n):
        x[i]=input("Enter x"+str(i)+" = ")
    for i in range(n):
         SimpleDifferenceTable[i][0]=input("Enter y"+str(i)+" = ")
    for i in range(1,n):
        for j in range(n-i):
            SimpleDifferenceTable[j][i]=SimpleDifferenceTable[j+1][i-1]-SimpleDifferenceTable[j][i-1]
    
    InterPolVal=float(input("Enter the interpolation value : "))
    p= ((InterPolVal-x[0])/(x[1]-x[0]))
    permap=p
    j=0 
    ans = float(SimpleDifferenceTable[0][0])      
    for i in range(n-1):
        if i == 0:
            trp=SimpleDifferenceTable[j][i+1]
            ans = ans + (p*SimpleDifferenceTable[j][i+1])
            print(" At n = "+str(i)+" the value is = " + str(ans))
        else :
            p=p*(permap-i)
            q=p
            trp=SimpleDifferenceTable[j][i+1]
            termer  = (q*(SimpleDifferenceTable[j][i+1])/math.factorial(i+1))
            ans = ans + (q*(SimpleDifferenceTable[j][i+1])/math.factorial(i+1))    
            print(" At n = "+str(i)+" the value is = " + str(ans))

    



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
        try:
            PInFunc=float(ReadyEq.evalf(subs={MainVar:p}))
        except:
            print("The value of the function became complex at P = " + str(p))
            return
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
# eq=input("Enter the equation :")
# tolerance=float(input("Enter the tolerance value = "))
# a=float(input("Enter the value of 'a' = "))
# b=float(input("Enter the value of 'b' = "))

# i=0
# for x in eq:
#     if eq[i]>='x' and eq[i]<='z':
#         MainVar=eq[i]
#         break
#     i=i+1

# print("The variable has been recognized as: " + MainVar)
# NewVar=symbols(MainVar) #Creates a sympy symbol named NewVar
# NewStr=MakeStringReady(eq)
# NewStr=sympify(NewStr)  #makes a sympy expression/equation
#LagrangeInterpolation()
#ForwardDifference()
ForWardsSDT();
#BackWardsSDT()
StirlingsMethod();
BackwardDifference()
# FixedPointIteration(NewStr,MainVar)
# Bisection(NewStr,MainVar)
# RegularFalsi(NewStr,MainVar)
# NewtonRaphson(NewStr,MainVar)
# Secant(NewStr,MainVar)
#DividedDifference()
i=0
# while i!=5:
#     TempStr=NewStr
#     print("The value of "+eq+" At x = "+ str(i) +" is:")
#     NewStr=sympify(NewStr)
#     print(NewStr.evalf(subs={MainVar:i}))
#     print('\n')
#     i=i+1

#MainWindow.mainloop();