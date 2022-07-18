# https://youtu.be/-rbozrj9poo

from z3 import *

carriages = []
for i in range(1, 12):
    carriages.append(Int(f'c{i}'))

s = Solver()

for i in range(len(carriages) - 2):
    s.add(carriages[i] + carriages[i + 1] + carriages[i + 2] == 99)

sum = 0
for i in range(len(carriages)):
    sum += carriages[i]

s.add(sum == 381)

print(s.check())
if s.check() == sat:
    print(s.model())

# sat
# [c3 = 15,
#  c7 = 0,
#  c1 = 0,
#  c2 = 84,
#  c5 = 84,
#  c4 = 0,
#  c9 = 15, <----
#  c6 = 15,
#  c11 = 84,
#  c8 = 84,
#  c10 = 0]
 
# 0 84 15 0 84 15 0 84 15 0 84