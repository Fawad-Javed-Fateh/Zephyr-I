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
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

def HeightChecker(height,n,points):
    f=str(points[0])
    Rounder=f[::-1].find('.')
    if Rounder<0:
        Rounder=0
    i=0
    while(i<n-1):
        if(round(points[i+1]-points[i],Rounder)!=height):
            return "Unequal Heights"
        i=i+1
    return "None"

def FindMainVar(equation):
    i=0
    for x in equation:
        if equation[i]>='x' and equation[i]<='z':
            MainVar=equation[i]
            break
        i=i+1
    return MainVar

def FindDoubleMainVar(equation):
    i=0
    MainVar=[]
    for x in equation:
        if equation[i]>='t' and equation[i]<='z':
            MainVar.append(equation[i])
        i=i+1
    MainVar=sorted(MainVar)
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
        elif equation[i]=='l' and equation[i+1]=='n':
            ParsableEq=ParsableEq+"ln("
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

def Bisection(equation,MainVar,a,b,tolerance,Chp2Table):
    Chp2Table.setRowCount(0)
    f=str(tolerance)
    Rounder=f[::-1].find('.')
    if Rounder<0:
        Rounder=0
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
    i=0
    while (AbsoluteError>tolerance):
        PosinFunc=float(equation.evalf(subs={MainVar:positive}))
        NeginFunc=float(equation.evalf(subs={MainVar:negative}))
        if PosinFunc*NeginFunc>0:
            return "None"
        c=round((negative+positive)/2,Rounder)
        AbsoluteError=round(math.fabs(c-prevc),Rounder)
        if AbsoluteError<tolerance:
            break
        Chp2Table.insertRow(Chp2Table.rowCount())
        Chp2Table.setItem(i, 0, QTableWidgetItem(str(i)))
        Chp2Table.setItem(i, 1, QTableWidgetItem(str(negative)))
        Chp2Table.setItem(i, 2, QTableWidgetItem(str(positive)))
        Chp2Table.setItem(i, 3, QTableWidgetItem(str(c)))
        Chp2Table.setItem(i, 5, QTableWidgetItem(str(AbsoluteError)))
        CinFunc=round(float(equation.evalf(subs={MainVar:c})),Rounder)
        Chp2Table.setItem(i, 4, QTableWidgetItem(str(CinFunc)))
        if CinFunc<0:
            negative=c
        else :
            positive=c
        prevc=c
        i=i+1
    Chp2Table.insertRow(Chp2Table.rowCount())
    Chp2Table.setItem(i, 0, QTableWidgetItem(str(i)))
    Chp2Table.setItem(i, 1, QTableWidgetItem(str(negative)))
    Chp2Table.setItem(i, 2, QTableWidgetItem(str(positive)))
    Chp2Table.setItem(i, 3, QTableWidgetItem(str(c)))
    Chp2Table.setItem(i, 4, QTableWidgetItem(str(CinFunc)))
    Chp2Table.setItem(i, 5, QTableWidgetItem(str(AbsoluteError)))
    return c

def RegularFalsi(equation,MainVar,a,b,tolerance,Chp2Table):
    Chp2Table.setRowCount(0)
    f=str(tolerance)
    Rounder=f[::-1].find('.')
    if Rounder<0:
        Rounder=0
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
    i=0
    while (AbsoluteError>tolerance):
          PosInFunc=float(equation.evalf(subs={MainVar:positive}))
          NegInFunc=float(equation.evalf(subs={MainVar:negative}))
          if (PosInFunc*NegInFunc>0):
              return "None"
          c=round((a*float(equation.evalf(subs={MainVar:b}))-b*float(equation.evalf(subs={MainVar:a}))),Rounder)
          c=round(c/(float(equation.evalf(subs={MainVar:b}))-float(equation.evalf(subs={MainVar:a}))),Rounder)
          AbsoluteError=round(math.fabs(c-prevc),Rounder)
          if AbsoluteError<tolerance:
            break
          Chp2Table.insertRow(Chp2Table.rowCount())
          Chp2Table.setItem(i, 0, QTableWidgetItem(str(i)))
          Chp2Table.setItem(i, 1, QTableWidgetItem(str(a)))
          Chp2Table.setItem(i, 2, QTableWidgetItem(str(b)))
          Chp2Table.setItem(i, 3, QTableWidgetItem(str(c)))
          Chp2Table.setItem(i, 5, QTableWidgetItem(str(AbsoluteError)))
          CinFunc=round(float(equation.evalf(subs={MainVar:c})),Rounder)
          Chp2Table.setItem(i, 4, QTableWidgetItem(str(CinFunc)))
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
    Chp2Table.insertRow(Chp2Table.rowCount())
    Chp2Table.setItem(i, 0, QTableWidgetItem(str(i)))
    Chp2Table.setItem(i, 1, QTableWidgetItem(str(a)))
    Chp2Table.setItem(i, 2, QTableWidgetItem(str(b)))
    Chp2Table.setItem(i, 3, QTableWidgetItem(str(c)))
    Chp2Table.setItem(i, 4, QTableWidgetItem(str(CinFunc)))
    Chp2Table.setItem(i, 5, QTableWidgetItem(str(AbsoluteError)))  
    return c 

def Secant(equation,MainVar,a,b,tolerance,Chp2Table):
    Chp2Table.setRowCount(0)
    f=str(tolerance)
    Rounder=f[::-1].find('.')
    if Rounder<0:
        Rounder=0
    AbsoluteError=1
    prevc=0
    i=0
    while(AbsoluteError>tolerance):
        c=round((a*float(equation.evalf(subs={MainVar:b}))-b*float(equation.evalf(subs={MainVar:a}))),Rounder)
        c=round(c/(float(equation.evalf(subs={MainVar:b}))-float(equation.evalf(subs={MainVar:a}))),Rounder)
        AbsoluteError=round(math.fabs(c-prevc),Rounder)
        Chp2Table.insertRow(Chp2Table.rowCount())
        Chp2Table.setItem(i, 0, QTableWidgetItem(str(i)))
        Chp2Table.setItem(i, 1, QTableWidgetItem(str(a)))
        Chp2Table.setItem(i, 2, QTableWidgetItem(str(b)))
        Chp2Table.setItem(i, 3, QTableWidgetItem(str(c)))
        Chp2Table.setItem(i, 5, QTableWidgetItem(str(AbsoluteError)))
        CinFunc=round(float(equation.evalf(subs={MainVar:c})),Rounder)
        Chp2Table.setItem(i, 4, QTableWidgetItem(str(CinFunc)))
        a=b
        b=c 
        i=i+1
        if(AbsoluteError<tolerance):
            break
        prevc=c 
    Chp2Table.insertRow(Chp2Table.rowCount())
    Chp2Table.setItem(i, 0, QTableWidgetItem(str(i)))
    Chp2Table.setItem(i, 1, QTableWidgetItem(str(a)))
    Chp2Table.setItem(i, 2, QTableWidgetItem(str(b)))
    Chp2Table.setItem(i, 3, QTableWidgetItem(str(c)))
    Chp2Table.setItem(i, 4, QTableWidgetItem(str(CinFunc)))
    Chp2Table.setItem(i, 5, QTableWidgetItem(str(AbsoluteError)))  
    return c

def NewtonRaphson(equation,MainVar,a,b,tolerance,Chp2Table):
    Chp2Table.setRowCount(0)
    f=str(tolerance)
    Rounder=f[::-1].find('.')
    if Rounder<0:
        Rounder=0
    AbsoluteError=1
    PrevP=0
    i=0
    p=float(a+b/2)
    while(AbsoluteError>tolerance):
        PInFunc=round(float(equation.evalf(subs={MainVar:p})),Rounder)
        DerEq=diff(equation,MainVar)
        PInDer=round(float(DerEq.evalf(subs={MainVar:p})),Rounder)
        PNext=round(float(p-(PInFunc/PInDer)),Rounder)
        AbsoluteError=round(math.fabs(PNext-PrevP),Rounder)
        Chp2Table.insertRow(Chp2Table.rowCount())
        Chp2Table.setItem(i, 0, QTableWidgetItem(str(i)))
        Chp2Table.setItem(i, 1, QTableWidgetItem(str(p)))
        Chp2Table.setItem(i, 2, QTableWidgetItem(str(PNext)))
        Chp2Table.setItem(i, 4, QTableWidgetItem(str(AbsoluteError)))
        Chp2Table.setItem(i, 3, QTableWidgetItem(str(PInFunc)))
        i=i+1
        if(AbsoluteError<tolerance):
            break
        PrevP=PNext
        p=PNext 
    Chp2Table.insertRow(Chp2Table.rowCount())
    Chp2Table.setItem(i, 0, QTableWidgetItem(str(i)))
    Chp2Table.setItem(i, 1, QTableWidgetItem(str(p)))
    Chp2Table.setItem(i, 2, QTableWidgetItem(str(PNext)))
    Chp2Table.setItem(i, 4, QTableWidgetItem(str(AbsoluteError)))
    Chp2Table.setItem(i, 3, QTableWidgetItem(str(PInFunc)))    
    return p

def FixedPointIteration(equation,MainVar,a,b,tolerance,Chp2Table):
    Chp2Table.setRowCount(0)
    f=str(tolerance)
    Rounder=f[::-1].find('.')
    if Rounder<0:
        Rounder=0
    ReadyEq=equation
    AbsoluteError=1
    PrevP=0
    i=0
    p=a
    errors = array('d',[a,a,a,a,a])
    #CummulativeAbsError=0
    while(AbsoluteError>tolerance):
        try:
            PInFunc=round(float(ReadyEq.evalf(subs={MainVar:p})),Rounder)
        except:
            return "Complex"
        AbsoluteError=round(math.fabs(PInFunc-PrevP),Rounder)
        Chp2Table.insertRow(Chp2Table.rowCount())
        Chp2Table.setItem(i, 0, QTableWidgetItem(str(i)))
        Chp2Table.setItem(i, 1, QTableWidgetItem(str(p)))
        Chp2Table.setItem(i, 3, QTableWidgetItem(str(AbsoluteError)))
        Chp2Table.setItem(i, 2, QTableWidgetItem(str(PInFunc)))
        errors.append(AbsoluteError)
        errors.pop(0)
        if(AbsoluteError<tolerance):
            break
        elif errors[4]==errors[2]:
            return "Bouncing"
            break
        elif (math.fabs(errors[4]-errors[3]) > math.fabs(errors[3]-errors[2])) and (math.fabs(errors[3]-errors[2]) > math.fabs(errors[2]-errors[1])) and math.fabs((errors[2]-errors[1]) > math.fabs(errors[1]-errors[0])):
            return "Divergent"
            break
        elif i>200:
            return "200 iterations"
            break
        i=i+1
        PrevP=PInFunc
        p=PInFunc
    Chp2Table.insertRow(Chp2Table.rowCount())
    Chp2Table.setItem(i, 0, QTableWidgetItem(str(i)))
    Chp2Table.setItem(i, 1, QTableWidgetItem(str(p)))
    Chp2Table.setItem(i, 3, QTableWidgetItem(str(AbsoluteError)))
    Chp2Table.setItem(i, 2, QTableWidgetItem(str(PInFunc)))
    return p

def LagrangeInterpolation(InterPolVal,n,argx,argy,Chp3interpolans):
    x=np.zeros(n,dtype=float)
    y=np.zeros(n,dtype=float)
    i=0
    for i in range(n):
        x[i]=argx[i]

    InterPol=InterPolVal
    for i in range(n):
        y[i]=argy[i]

    f=str(argy[1])
    Rounder=f[::-1].find('.')
    if Rounder<0:
        Rounder=0

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
                result=round(result,Rounder)
            Chp3interpolans.append("\nThe " + str(i) + " Degree Polynomial is: " + str(round(result,Rounder)))
    return result   

def DividedDifference(n,Xpoints,ypoints,eq,InterPol,DifferenceTable,Chp3interpolans):
    Chp3interpolans.setPlainText("")
    DifferenceTable.setColumnCount(n+1)
    DifferenceTable.setRowCount(2*n-1)
    Ypoint = []
    f=str(ypoints[0])
    Rounder=f[::-1].find('.')
    if Rounder<0:
        Rounder=0
    i=0    
    if (ypoints[0]==0 and ypoints[1]==0):
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
            Ypoint.append(ypoints[i])
            i=i+1
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
    i=0
    for i in range(n):
        DifferenceTable.setItem(2*i,0, QTableWidgetItem(str(Xpoints[i])))
        DifferenceTable.setItem(2*i,1, QTableWidgetItem(str(Ypoints[0][i])))

    for i in range(1,n):
        for j in range(0,n-i):
            DifferenceTable.setItem(2*j+i,i+1, QTableWidgetItem(str(Ypoints[i][j])))
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
        Chp3interpolans.append("\nThe " + str(i) + " Degree Polynomial is: " + str(round(Answer,Rounder)))
        i=i+1
    return round(Answer,Rounder)

def ForwardDifference(n,Xpoints,ypoints,eq,InterPol,DifferenceTable,Chp3interpolans):
    Chp3interpolans.setPlainText("")
    DifferenceTable.setColumnCount(n+1)
    DifferenceTable.setRowCount(2*n-1)
    Ypoint = []
    f=str(Xpoints[0])
    Rounder=f[::-1].find('.')
    if Rounder<0:
        Rounder=0
    height=round(Xpoints[1]-Xpoints[0],Rounder)
    status=HeightChecker(height,n,Xpoints)
    if(status=="Unequal Heights"):
        return status
    i=0
    if (ypoints[0]==0 and ypoints[1]==0):
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
            Ypoint.append(ypoints[i])
            i=i+1
    f=str(Ypoint[0])
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
    i=0
    for i in range(n):
        DifferenceTable.setItem(2*i,0, QTableWidgetItem(str(Xpoints[i])))
        DifferenceTable.setItem(2*i,1, QTableWidgetItem(str(Ypoints[0][i])))

    for i in range(1,n):
        for j in range(0,n-i):
            DifferenceTable.setItem(2*j+i,i+1, QTableWidgetItem(str(Ypoints[i][j])))
            
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
        Answer=Answer+Aval
        Chp3interpolans.append("\nThe " + str(i) + " Degree Polynomial is: " + str(round(Answer,Rounder)))
        i=i+1
    return round(Answer,Rounder)

def BackwardDifference(n,Xpoints,ypoints,eq,InterPol,DifferenceTable,Chp3interpolans):
    Chp3interpolans.setPlainText("")
    DifferenceTable.setColumnCount(n+1)
    DifferenceTable.setRowCount(2*n-1)
    Ypoint = []
    f=str(Xpoints[0])
    Rounder=f[::-1].find('.')
    if Rounder<0:
        Rounder=0
    height=round(Xpoints[1]-Xpoints[0],Rounder)
    status=HeightChecker(height,n,Xpoints)
    if(status=="Unequal Heights"):
        return status
    i=0   
    if (ypoints[0]==0 and ypoints[1]==0):
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
            Ypoint.append(ypoints[i])
            i=i+1
    f=str(Ypoint[0])
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
    i=0
    for i in range(n):
        DifferenceTable.setItem(2*i,0, QTableWidgetItem(str(Xpoints[i])))
        DifferenceTable.setItem(2*i,1, QTableWidgetItem(str(Ypoints[0][i])))

    for i in range(1,n):
        for j in range(0,n-i):
            DifferenceTable.setItem(2*j+i,i+1, QTableWidgetItem(str(Ypoints[i][j])))

    Var_S=round((InterPol-Xpoints[n-1])/height,Rounder)

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
        Chp3interpolans.append("\nThe " + str(i) + " Degree Polynomial is: " + str(round(Answer,Rounder)))
        i=i+1
    return round(Answer,Rounder)

def StirlingsMethod(InterPolVal,n,argx,argy,DifferenceTable):
    f=str(argy[0])
    Rounder=f[::-1].find('.')
    if Rounder<0:
        Rounder=0
    DifferenceTable.setRowCount(2*n-1)
    x=np.zeros(n,dtype=float)
    y=np.zeros(n,dtype=float)
    SimpleDifferenceTable=np.zeros((n,n),dtype=float)
    for i in range(n):
        x[i]=argx[i]
        SimpleDifferenceTable[i][0]=argy[i]
        DifferenceTable.setItem(2*i,0, QTableWidgetItem(str(x[i])))
        DifferenceTable.setItem(2*i,1, QTableWidgetItem(str(SimpleDifferenceTable[i][0])))
    height=x[1]-x[0]
    height=round(height,n)
    status=HeightChecker(height,n,x)
    if status=="Unequal Heights":
        return status
    for i in range(1,n):
        for j in range(0,n-i):
            SimpleDifferenceTable[j][i]=round(SimpleDifferenceTable[j+1][i-1]-SimpleDifferenceTable[j][i-1],Rounder)
            DifferenceTable.setItem(2*j+i,i+1, QTableWidgetItem(str(SimpleDifferenceTable[j][i])))
    diff=x[1]-x[0]  
    MidTerm=math.floor(n/2)  
    p=float((InterPolVal-x[MidTerm])/diff) 
    ans=float(SimpleDifferenceTable[MidTerm][0])
    ans=round(ans,Rounder)
    ans=ans+float(p*((SimpleDifferenceTable[MidTerm][1]+SimpleDifferenceTable[MidTerm-1][1])/2))
    ans=round(ans,Rounder)
    MidTerm=MidTerm-1
    ans=round(ans,Rounder)
    padder=2
    oddcump=1
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
            ans=round(ans,Rounder)
            if MidTerm!=0:
                MidTerm=MidTerm-1
            oddcump=1
            if i!=2:
                padder=padder+1
        if i%2!=0:
            for j in range(1,padder,1):
                oddcump=oddcump*((p**2)-(j**2))
            oddcump=p*oddcump;
            oddcump=round(oddcump,Rounder)
            tmid=int(0)
            for k in range(n):
                if(SimpleDifferenceTable[k][i]!=0):
                    tmid=tmid+1
            tmid=int(tmid/2)
            ans=ans+((oddcump/math.factorial(i))*((SimpleDifferenceTable[tmid][i]+SimpleDifferenceTable[tmid-1][i])/2))
            oddcump=1
            ans=round(ans,Rounder)
            padder=padder+1
            if MidTerm!=0:
                MidTerm=MidTerm-1
    return ans
     

def BackWardsSDT(InterPolVal,n,argx,argy,DifferenceTable,Chp3interpolans):
    DifferenceTable.setRowCount(n)
    x=np.zeros(n,dtype=float)
    y=np.zeros(n,dtype=float)
    SimpleDifferenceTable=np.zeros((n,n),dtype=float)
    for i in range(n):
        x[i]=argx[i]
    for i in range(n):
         SimpleDifferenceTable[i][0]=argy[i]
    height=x[1]-x[0]
    height=round(height,n)
    status=HeightChecker(height,n,x)
    if status=="Unequal Heights":
        return status
    f=str(argy[0])
    Rounder=f[::-1].find('.')
    if Rounder<0:
        Rounder=0
    for i in range(1,n):
        for j in range(0,n-i):
            SimpleDifferenceTable[j][i]=SimpleDifferenceTable[j+1][i-1]-SimpleDifferenceTable[j][i-1]
            SimpleDifferenceTable[j][i]=round(SimpleDifferenceTable[j][i],Rounder)
            DifferenceTable.setItem(j,i, QTableWidgetItem(str(SimpleDifferenceTable[j][i])))
    
    p= ((InterPolVal-x[n-1])/(x[1]-x[0]))
    p=round(p,Rounder)
    permap=p
    j=n-2 
    ans = float(SimpleDifferenceTable[n-1][0])
    ans=round(ans,Rounder)      
    for i in range(n-1):
        if i == 0:
            trp=SimpleDifferenceTable[j][i+1]
            ans = ans + (p*SimpleDifferenceTable[j][i+1])
            print(" At n = "+str(i)+" the value is = " + str(ans))
            ans=round(ans,Rounder)
            Chp3interpolans.append("\nThe " + str(i) + " Degree Polynomial is: " + str(ans))
            j=j-1
        else :
            p=p*(permap+i)
            q=p
            trp=SimpleDifferenceTable[j][i+1]
            termer  = (q*(SimpleDifferenceTable[j][i+1])/math.factorial(i+1))
            ans = ans + (q*(SimpleDifferenceTable[j][i+1])/math.factorial(i+1))
            ans=round(ans,Rounder)
            j=j-1    
            Chp3interpolans.append("\nThe " + str(i) + " Degree Polynomial is: " + str(ans))
            print(" At n = "+str(i)+" the value is = " + str(ans))
    return ans 

def ForWardsSDT(InterPolVal,n,argx,argy,DifferenceTable,Chp3interpolans):
    DifferenceTable.setRowCount(n)
    x=np.zeros(n,dtype=float)
    y=np.zeros(n,dtype=float)
    SimpleDifferenceTable=np.zeros((n,n),dtype=float)
    for i in range(n):
        x[i]=argx[i]
    for i in range(n):
         SimpleDifferenceTable[i][0]=argy[i]
    f=str(argy[0])
    Rounder=f[::-1].find('.')
    if Rounder<0:
        Rounder=0
    height=x[1]-x[0]
    height=round(height,n)
    status=HeightChecker(height,n,x)
    if status=="Unequal Heights":
        return status
    for i in range(1,n):
        for j in range(0,n-i):
            SimpleDifferenceTable[j][i]=SimpleDifferenceTable[j+1][i-1]-SimpleDifferenceTable[j][i-1]
            SimpleDifferenceTable[j][i]=round(SimpleDifferenceTable[j][i],Rounder)
            DifferenceTable.setItem(j,i, QTableWidgetItem(str(SimpleDifferenceTable[j][i])))
    
    p= ((InterPolVal-x[0])/(x[1]-x[0]))
    p=round(p,Rounder)
    permap=p
    j=0 
    ans = float(SimpleDifferenceTable[0][0])   
    ans=round(ans,Rounder)   
    for i in range(n-1):
        if i == 0:
            trp=SimpleDifferenceTable[j][i+1]
            ans = ans + (p*SimpleDifferenceTable[j][i+1])
            ans=round(ans,Rounder)
            Chp3interpolans.append("\nThe " + str(i) + " Degree Polynomial is: " + str(ans))
            print(" At n = "+str(i)+" the value is = " + str(ans))
        else :
            p=p*(permap-i)
            q=p
            trp=SimpleDifferenceTable[j][i+1]
            termer  = (q*(SimpleDifferenceTable[j][i+1])/math.factorial(i+1))
            ans = ans + (q*(SimpleDifferenceTable[j][i+1])/math.factorial(i+1))    
            ans=round(ans,Rounder)
            Chp3interpolans.append("\nThe " + str(i) + " Degree Polynomial is: " + str(ans))
            print(" At n = "+str(i)+" the value is = " + str(ans))
    return ans 

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
        yi=yi+k
        ti=ti+h
        print(str(ti)+ "    "+ str(yi))



#MainWindow=tk.Tk()
# eq=input("Enter the equation :")
#CompositeSimpson()
#CompositeMidPoint()
#EulerMethod()
# tolerance=float(input("Enter the tolerance value = "))
# a=float(input("Enter the value of 'a' = "))
# b=float(input("Enter the value of 'b' = "))
#ThreePointDifferentiation()
#ForwardsDifferentiation()
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
#ForWardsSDT();
#BackWardsSDT()
#StirlingsMethod();
#BackwardDifference()
# FixedPointIteration(NewStr,MainVar)
# Bisection(NewStr,MainVar)
# RegularFalsi(NewStr,MainVar)
# NewtonRaphson(NewStr,MainVar)
# Secant(NewStr,MainVar)
#DividedDifference()
#i=0
# while i!=5:
#     TempStr=NewStr
#     print("The value of "+eq+" At x = "+ str(i) +" is:")
#     NewStr=sympify(NewStr)
#     print(NewStr.evalf(subs={MainVar:i}))
#     print('\n')
#     i=i+1

#MainWindow.mainloop();