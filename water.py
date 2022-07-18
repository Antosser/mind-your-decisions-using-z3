# https://youtu.be/2TBQiV3onNU

from z3 import *

n, h = Reals('n h')

s = Solver()

def parabola(x):
    return (x ** 2 * (-1)) * n + 3

s.add(parabola(2) == 0)
s.add(h == parabola(-1))

print(s.check())
if s.check() == sat:
    print(s.model())
    
# sat
# [n = 3/4, h = 9/4]

# 9/4 -> 2.25