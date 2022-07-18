# https://youtu.be/kQ_Nl-OH5oc

from z3 import *

x, y, d = Ints('x y d')

s = Solver()

s.add(x >= 0, x <= 9)
s.add(y >= 0, y <= 9)

s.add((x * 10000 + 6790 + y) % 72 == 0)

print(s.check())
if s.check() == sat:
    print(s.model())

# sat
# [x = 3, y = 2]

# $36792 / 72 = $511