import sympy as sp
from sympy.solvers import solveset
from sympy import Symbol
from sympy import var
from sympy import sympify
from sympy import Eq
import math
from sympy import *
x=symbols('x')
exp=230*x**4
print(type(exp))
print(type(x))
print(exp.subs(x,4))
print(exp.evalf(subs={x:4}))