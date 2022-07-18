# https://youtu.be/ZbXb5jy-NQ4

from z3 import *

a, b = Ints('a b')

s = Solver()

s.add(a >= 0, a <= 9)
s.add(b >= 0, b <= 9)

m1 = a * 10 + b
m2 = b * 10 + a

s.add(m1 * m2 == 2944)

print(s.check())
if s.check() == sat:
    print(s.model())
    
# sat
# [b = 4, a = 6]

#   64
# X 46
# ----
# 2944