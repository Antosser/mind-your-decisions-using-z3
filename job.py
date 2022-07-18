# https://youtu.be/ABj3IC9pYlQ

from z3 import *

a, b, c, n = Reals('a b c n')

s = Solver()

s.add(a * 2 + b * 2 == 1)
s.add(a * 3 + c * 3 == 1)
s.add(b * 4 + c * 4 == 1)
s.add(a * n + b * n + c * n == 1)

print(s.check())
if s.check() == sat:
    print(s.model())
    
# sat
# [n = 24/13, a = 7/24, b = 5/24, c = 1/24]

# 24/13 -> 1.84615385 -> 110.76 minutes