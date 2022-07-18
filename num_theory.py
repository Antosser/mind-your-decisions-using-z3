# https://youtu.be/sHZqOmDOBZM

from z3 import *

x, y, z = Ints('x y z')

s = Solver()

s.add(3 ** x + 4 ** y == 5 ** z)

print(s.check())
while s.check() == sat:
  sol = s.model()
  print(sol)
  s.add(Not(And(
      x == sol[x],
      y == sol[y],
      z == sol[z]
  )))

# unknown