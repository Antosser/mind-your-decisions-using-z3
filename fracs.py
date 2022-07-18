# https://youtu.be/C8M_ErBgCV8

from z3 import *

m, n = Ints('m n')

s = Solver()

s.add((5 + (3 / m)) * (n + (1 / 2)) == 19)
s.add(m > 0, m <= 9)
s.add(n >= 0, n <= 9)

print(s.check())
if s.check() == sat:
    print(s.model())
    
# unsat

# why???