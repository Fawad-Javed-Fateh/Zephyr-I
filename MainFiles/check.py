import sympy as sp
from sympy.solvers import solveset
from sympy import Symbol
from sympy import var
from sympy import sympify
from sympy import Eq
import math
from sympy import *
x=symbols('x')
exp=ln(x-1)
c=(diff(exp,x))
print(str(c))