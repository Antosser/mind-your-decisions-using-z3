# https://youtu.be/4FNCIYD8HdA

from z3 import *

x, y, z, n = Reals('x y z n')

s = Solver()

s.add(x + y + z == 1)
s.add(x ** 2 + y ** 2 + z ** 2 == 2)
s.add(x ** 3 + y ** 3 + z ** 3 == 3)
s.add(x ** 5 + y ** 5 + z ** 5 == n)

print(s.check())
if s.check() == sat:
    print(s.model())
    
# unsat