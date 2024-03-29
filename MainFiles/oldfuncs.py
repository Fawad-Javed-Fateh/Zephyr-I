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

def ForwardsDifferentiation():
    n=int(input("Enter the total number of data points "))
    eq=str(input("Enter the equation "))
    eq=MakeStringReady(eq)
    MainVar=FindMainVar(eq)
    eq=sympify(eq)
    MainVar=symbols(MainVar)
    x=np.zeros(n,dtype=float)    
    y=np.zeros(n,dtype=float)
    h=float(x[1]-x[0])
    for i in range(n):
        y[i]=float(eq.evalf(subs={MainVar:x[i]}))
    for i in range(n):
        if i != n-1:
            val=float(x[i]+h)
            p1=float(eq.evalf(subs={MainVar:val}))
            p2=float(eq.evalf(subs={MainVar:x[i]}))
            ans=float(p1-p2)
            ans=float(ans/h)
            print("dx/dy(" +str(x[i]) + ") = " + str(ans))
        elif i == n-1:
            val=float(x[i]-h)
            p1=float(eq.evalf(subs={MainVar:val}))
            p2=float(eq.evalf(subs={MainVar:x[i]}))
            ans=float(p2-p1)
            ans=float(ans/h)
            print("dx/dy(" +str(x[i]) + ") = " + str(ans))

def ThreePointDifferentiation():
    n=int(input("Enter the number of points "))
    x=np.zeros(n,dtype=float)
    y=np.zeros(n,dtype=float)
    print("Start entering x values: ")
    for i in range(n):
        x[i]=float(input("x" +str(i) + " = "))
    eq=input("Enter the equation : ")
    eq=MakeStringReady(eq)
    MainVar=FindMainVar(eq)
    eq=sympify(eq)
    MainVar=symbols(MainVar)
    h=x[1]-x[0]
    for i in range(n):
        y[i]=float(eq.evalf(subs={MainVar:x[i]}))
    if n%2==0:
        m2=n/2
        m1=m2-1
        for i in range(n):
            if i < m1 and i < m2 :
                ans=float(-3*(y[i])+4*(y[i+1])-(y[i+2]))
                ans=ans/(2*h)
                print("dx/dy(x" + str(i) +") = " + str(ans))
            if i == m1 or i == m2:
                ans=float(y[i+1]-y[i-1])
                ans=ans/(2*h)
                print("dx/dy(x" + str(i) +") = " + str(ans))
            if i > m1 and i > m2 :
                ans=float(-3*(y[i])+4*(y[i-1])-(y[i-2]))
                q=h-2*h
                ans=ans/(2*q)
                print("dx/dy(x" + str(i) +") = " + str(ans))
    else:
        m=math.floor(n/2)
        for i in range(n):
            if i < m :
                ans=float(-3*(y[i])+4*(y[i+1])-(y[i+2]))
                ans=ans/(2*h)
                print("dx/dy(x" + str(i) +") = " + str(ans))
            if i == m:
                ans=float(y[i+1]-y[i-1])
                ans=ans/(2*h)
                print("dx/dy(x" + str(i) +") = " + str(ans))
            if i > m :
                ans=float(-3*(y[i])+4*(y[i-1])-(y[i-2]))
                q=h-2*h
                ans=ans/(2*q)
                print("dx/dy(x" + str(i) +") = " + str(ans))

def FivePointDifferentiation():
    n=int(input("Enter the number of points "))
    Xpoints=[]
    Ypoints=[]
    print("Start entering x values: ")
    for i in range(n):
        Xpoints.append(float(input("x" +str(i) + " = ")))
    # eq=input("Enter the equation : ")
    # eq=MakeStringReady(eq)
    # MainVar=FindMainVar(eq)
    # eq=sympify(eq)
    # MainVar=symbols(MainVar)
    height=Xpoints[1]-Xpoints[0]
    for i in range(n):
        # Ypoints.append(float(eq.evalf(subs={MainVar:Xpoints[i]})))
        Ypoints.append(float(input("Enter point:")))
    i=0
    DerivList=[None]*(n)
    while (i<n):
        #the endpoint
        if(i+5<=n):  
            DerivAns=0
            DerivAns+=-25*Ypoints[i]
            DerivAns+=48*Ypoints[i+1]
            DerivAns+=-36*Ypoints[i+2]
            DerivAns+=16*Ypoints[i+3]
            DerivAns+=-3*Ypoints[i+4]
            DerivAns=DerivAns/(12*height)
        elif (i-4>=0):
            DerivAns=0
            DerivAns+=-25*Ypoints[i]
            DerivAns+=48*Ypoints[i-1]
            DerivAns+=-36*Ypoints[i-2]
            DerivAns+=16*Ypoints[i-3]
            DerivAns+=-3*Ypoints[i-4]
            DerivAns=DerivAns/(12*height)
        else:
            DerivAns=0
            DerivAns+=Ypoints[i-2]
            DerivAns+=-8*Ypoints[i-1]
            DerivAns+=8*Ypoints[i+1]
            DerivAns+=-1*Ypoints[i+2]
            DerivAns=DerivAns/(12*height)
        print(str(DerivAns))
        DerivList[i]=DerivAns
        i=i+1

def DoubleDerivativeMidpoint():
    n=int(input("Enter the number of points "))
    Xpoints=[]
    Ypoints=[]
    print("Start entering x values: ")
    for i in range(n):
        Xpoints.append(float(input("x" +str(i) + " = ")))
    # eq=input("Enter the equation : ")
    # eq=MakeStringReady(eq)
    # MainVar=FindMainVar(eq)
    # eq=sympify(eq)
    # MainVar=symbols(MainVar)
    height=Xpoints[1]-Xpoints[0]
    for i in range(n):
        # Ypoints.append(float(eq.evalf(subs={MainVar:Xpoints[i]})))
        Ypoints.append(float(input("Enter point:")))
    Deriv2List=[None]*(n)
    i=0
    while(i<n):
        Derivative2=0
        if(i>0 and i<(n-1)):
            Derivative2+=Ypoints[i-1]
            Derivative2+=-2*Ypoints[i]
            Derivative2+=Ypoints[i+1]
            Derivative2=Derivative2/(height*height)
        print(str(Derivative2))
        Deriv2List[i]=DerivAns
        i=i+1

def CompositeTrapezodial():
    a=float(input("Enter the upper limit : "))
    b=float(input("Enter the lower limit : "))
    h=float(input("Enter the value of h (difference) : "))
    eq=str(input("Enter the equation : "))
    eq=MakeStringReady(eq)
    MainVar=FindMainVar(eq)
    eq=sympify(eq)
    MainVar=symbols(MainVar)  
    n=int((a-b)/h)
    n=n+1
    x=np.zeros(n,dtype=float)
    y=np.zeros(n,dtype=float)
    x[0]=b
    for i in range(1,n):
        x[i]=x[i-1]+h
    for i in range(n):
        y[i]=float(eq.evalf(subs={MainVar:x[i]}))
    ans=float(0)
    ans=float(y[0]+y[n-1])
    temp=float(0)
    for i in range(1,n-1):
        print(str(x[i]))
        temp=temp+y[i]
    temp=temp*2
    ans=ans+temp
    ans=ans*(h/2)
    print("The ans is = " + str(ans))

def CompositeSimpson():
    a=float(input("Enter the upper limit : "))
    b=float(input("Enter the lower limit : "))
    h=float(input("Enter the value of h (difference) : "))
    eq=str(input("Enter the equation : "))
    eq=MakeStringReady(eq)
    MainVar=FindMainVar(eq)
    eq=sympify(eq)
    MainVar=symbols(MainVar)  
    n=int((a-b)/h)
    n=n+1
    x=np.zeros(n,dtype=float)
    y=np.zeros(n,dtype=float)
    x[0]=b
    for i in range(1,n):
        x[i]=x[i-1]+h
    for i in range(n):
        y[i]=float(eq.evalf(subs={MainVar:x[i]}))
    ans=float(0)
    ans=float(y[0]+y[n-1])
    temp1=float(0)
    temp2=float(0)
    for i in range(1,n-1):
        if i%2==0:
            temp1=temp1+y[i]
        else:
            temp2=temp2+y[i]
    temp1=temp1*2
    temp2=temp2*4
    ans=ans+temp2+temp1
    ans=ans*(h/3)
    print("The ans is = " + str(ans))    

def CompositeMidPoint():
    a=float(input("Enter the upper limit : "))
    b=float(input("Enter the lower limit : "))
    h=float(input("Enter the value of h (difference) : "))
    eq=str(input("Enter the equation : "))
    eq=MakeStringReady(eq)
    MainVar=FindMainVar(eq)
    eq=sympify(eq)
    MainVar=symbols(MainVar)  
    n=int((a-b)/h)
    n=n+1
    x=np.zeros(n,dtype=float)
    y=np.zeros(n,dtype=float)
    x[0]=b
    for i in range(1,n):
        x[i]=x[i-1]+h
    for i in range(n):
        y[i]=float(eq.evalf(subs={MainVar:x[i]}))
    ans=float(0)
    for i in range(1,n,2):
        print(str(x[i]))
        ans=ans+y[i]
    ans=ans*(2*h)
    print("The ans is = " + str(ans))    



def Bisection2(equation,MainVar,a,b,tolerance):
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
    
    Var_S=round((InterPol-Xpoints[Xpoints.__len__()-1])/height,Rounder)

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
        Answer=Answer+Aval
        print(Answer)
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

def StirlingsMethod():
    #Rounder=f[::-1].find('.')
    n=int(input("Enter total number of data points "))
    x=np.zeros(n,dtype=float)
    y=np.zeros(n,dtype=float)
    SimpleDifferenceTable=np.zeros((n,n),dtype=float)
    print("Start entering x values, they must have equal spacing for simple difference ")
    for i in range(n):
         x[i]=input("Enter x"+str(i)+" = ")
    # SimpleDifferenceTable[0][0]=0.7651977
    # SimpleDifferenceTable[1][0]=0.6200860
    # SimpleDifferenceTable[2][0]=0.4554022
    # SimpleDifferenceTable[3][0]=0.2818186
    # SimpleDifferenceTable[4][0]=0.1103623
    # x[0]=1.0
    # x[1]=1.3
    # x[2]=1.6
    # x[3]=1.9
    # x[4]=2.2


    for i in range(n):
        SimpleDifferenceTable[i][0]=input("Enter y"+str(i)+" = ") 
    for i in range(1,n):
        for j in range(0,n-i):
            SimpleDifferenceTable[j][i]=SimpleDifferenceTable[j+1][i-1]-SimpleDifferenceTable[j][i-1]
    for i in range(n-1):
        for j in range(n-1):
            print(str(SimpleDifferenceTable[i][j])+" ")
        print("\n")
    InterPolVal=float(input("Enter the interpolation value "))
    diff=x[1]-x[0]  
    MidTerm=math.floor(n/2)  
    p=float((InterPolVal-x[MidTerm])/diff) 
    ans=float(SimpleDifferenceTable[MidTerm][0])
    ans=ans+float(p*((SimpleDifferenceTable[MidTerm][1]+SimpleDifferenceTable[MidTerm-1][1])/2))
    MidTerm=MidTerm-1
    ans=round(ans,5)
    padder=2;
    oddcump=1;
    for i in range(2,n,1):
        if i%2==0:
            if i!=2:
                for j in range(1,padder,1):
                    oddcump=oddcump*((p**2)-(j**2))
            oddcump=(p**2)*oddcump
            oddcump=round(oddcump,5)
            tmid=int(0)
            for k in range(n):
                if(SimpleDifferenceTable[k][i]!=0):
                    tmid=tmid+1
            tmid=math.floor(tmid/2)
            ans=ans+((oddcump/math.factorial(i))*SimpleDifferenceTable[tmid][i])
            ans=round(ans,5)
            if MidTerm!=0:
                MidTerm=MidTerm-1
            oddcump=1
            if i!=2:
                padder=padder+1
        if i%2!=0:
            for j in range(1,padder,1):
                oddcump=oddcump*((p**2)-(j**2))
            oddcump=p*oddcump;
            oddcump=round(oddcump,5)
            tmid=int(0)
            for k in range(n):
                if(SimpleDifferenceTable[k][i]!=0):
                    tmid=tmid+1
            tmid=int(tmid/2)
            ans=ans+((oddcump/math.factorial(i))*((SimpleDifferenceTable[tmid][i]+SimpleDifferenceTable[tmid-1][i])/2))
            oddcump=1
            ans=round(ans,5)
            padder=padder+1
            if MidTerm!=0:
                MidTerm=MidTerm-1
    print("The generic ans = "+ str(ans))



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

def EulerMethod():
    eq=str(input("Enter the differential equation : y'="))
    eq=MakeStringReady(eq)
    MainVars=FindDoubleMainVar(eq)
    Y=symbols('y')
    T=symbols('t')
    eq=sympify(eq)
    h=float(input("Enter the value of h : "))
    yi=float(input("Enter the inital value of y : "))
    ti=float(input("Enter the inital value of t : "))
    tf=float(input("Enter the final value of t : "))
    print(str(ti)+ "    "+ str(yi))
    while ti!=tf:
        k=h*float(eq.evalf(subs={Y:yi,T:ti}))
        k=round(k,7)
        yi=yi+k
        yi=round(yi,7)
        ti=ti+h
        ti=round(ti,2)
        print(str(ti)+ "    "+ str(yi))

def ModifiedEulerMethod():
    eq=str(input("Enter the differential equation : y'="))
    eq=MakeStringReady(eq)
    MainVars=FindDoubleMainVar(eq)
    Y=symbols('y')
    T=symbols('t')
    eq=sympify(eq)
    h=float(input("Enter the value of h : "))
    yi=float(input("Enter the inital value of y : "))
    ti=float(input("Enter the inital value of t : "))
    tf=float(input("Enter the final value of t : "))
    print(str(ti)+ "              "+ str(yi))
    while ti!=tf:
        k1=h*float(eq.evalf(subs={Y:yi,T:ti}))
        k1=round(k1,7)
        k2=h*float(eq.evalf(subs={Y:yi+k1,T:ti+h}))
        k2=round(k2,7)
        yi=yi+0.5*(k1+k2)
        yi=round(yi,7)
        ti=ti+h
        ti=round(ti,2)
        print(str(ti)+ "    "+ str(yi))

def MidpointMethod():
    eq=str(input("Enter the differential equation : y'="))
    eq=MakeStringReady(eq)
    MainVars=FindDoubleMainVar(eq)
    Y=symbols('y')
    T=symbols('t')
    eq=sympify(eq)
    h=float(input("Enter the value of h : "))
    yi=float(input("Enter the inital value of y : "))
    ti=float(input("Enter the inital value of t : "))
    tf=float(input("Enter the final value of t : "))
    print(str(ti)+ "    "+ str(yi))
    while ti!=tf:
        k1=float(eq.evalf(subs={Y:yi,T:ti}))
        k1=round(k1,7)
        k2=float(eq.evalf(subs={Y:yi+((h/2)*k1),T:ti+(h/2)}))
        k2=round(k2,7)
        yi=yi+h*(k2)
        yi=round(yi,7)
        ti=ti+h
        ti=round(ti,2)
        print(str(ti)+ "    "+ str(yi))

def HeunsMethod():
    eq=str(input("Enter the differential equation : y'="))
    eq=MakeStringReady(eq)
    MainVars=FindDoubleMainVar(eq)
    Y=symbols('y')
    T=symbols('t')
    eq=sympify(eq)
    h=float(input("Enter the value of h : "))
    h=round(h,2)
    yi=float(input("Enter the inital value of y : "))
    ti=float(input("Enter the inital value of t : "))
    tf=float(input("Enter the final value of t : "))
    print(str(ti)+ "    "+ str(yi))
    while ti!=tf:
        k1=float(eq.evalf(subs={Y:yi,T:ti}))
        k1=round(k1,7)
        k2=float(eq.evalf(subs={Y:yi+((h/3)*k1),T:ti+(h/3)}))
        k2=round(k2,7)
        k3=float(eq.evalf(subs={Y:yi+(((2*h)/3)*k2),T:ti+((2*h)/3)}))
        k3=round(k3,7)        
        yi=yi+(h/4)*(k1+(3*k3))
        yi=round(yi,7)
        ti=ti+h
        ti=round(ti,2)
        print(str(ti)+ "    "+ str(yi))

def RungeKuttaMethod():
    eq=str(input("Enter the differential equation : y'="))
    eq=MakeStringReady(eq)
    MainVars=FindDoubleMainVar(eq)
    Y=symbols('y')
    T=symbols('t')
    eq=sympify(eq)
    h=float(input("Enter the value of h : "))
    h=round(h,2)
    yi=float(input("Enter the inital value of y : "))
    ti=float(input("Enter the inital value of t : "))
    tf=float(input("Enter the final value of t : "))
    print(str(ti)+ "    "+ str(yi))
    while ti!=tf:
        k1=h*float(eq.evalf(subs={Y:yi,T:ti}))
        k1=round(k1,7)
        k2=h*float(eq.evalf(subs={Y:yi+((1/2)*k1),T:ti+(h/2)}))
        k2=round(k2,7)
        k3=h*float(eq.evalf(subs={Y:yi+((1/2)*k2),T:ti+((h)/2)}))
        k3=round(k3,7)        
        k4=h*float(eq.evalf(subs={Y:yi+k3,T:ti+h}))
        k4=round(k4,7)
        yi=yi+(1/6)*(k1+(2*k2)+(2*k3)+k4)
        yi=round(yi,7)
        ti=ti+h
        ti=round(ti,2)
        print(str(ti)+ "    "+ str(yi))

