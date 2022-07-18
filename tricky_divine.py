# https://youtu.be/3jnbBVpOf40

from z3 import *

x = Real('x')

s = Solver()

s.add((x - 1 / x) ** (1/2) + (1 - 1 / x) ** (1/2) == x)

print(s.check())
if s.check() == sat:
    print(s.model())
    
# unknown