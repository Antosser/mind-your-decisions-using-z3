# https://youtu.be/Pb7N6wqhjhg

from z3 import *

a, b, c, x = Reals('a b c x')

s = Solver()

def f(x):
    return a * x ** 2 + b * x + c

s.add(f(1) == 5, f(2) == 10, f(3) == 55)
s.add(x == f(10))

print(s.check())
if s.check() == sat:
    print(s.model())
    
# sat
# [c = 40, a = 20, b = -55, x = 1490]

# 1490