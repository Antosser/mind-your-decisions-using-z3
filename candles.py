# https://youtu.be/8vODMR9m_Uw

from z3 import *

c1, c2, t, s = Reals('c1 c2 t s')

s = Solver()

s.add(c1 == 1 - t / 8)
s.add(c2 == 1 - t / 10)
s.add(c1 > 0)
s.add(c2 > 0)

s.add(c1 * 2 == c2)

print(s.check())
if s.check() == sat:
    print(s.model())
    
# sat
# [t = 20/3, c1 = 1/6, c2 = 1/3]

# 20/3 -> 6.66 hours -> 6 hours 40 minutes