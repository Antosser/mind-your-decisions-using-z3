# https://youtu.be/6F6hw_U-AX4

from z3 import *

x, y = Ints('x y')

s = Solver()

s.add(x > 9)
s.add(y > 2)

s.add(9 + x == 2 * y + 1)

print(s.check())
if s.check() == sat:
    print(s.model())

# sat
# [y = 9, x = 10]

# 9 + 10  ==  21
# base 10   base 9