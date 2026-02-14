from z3 import *

Student = DeclareSort('Student')

a = Const("a", Student)

E = Function("E", Student, BoolSort())
B = Function("B", Student, BoolSort())

clauses = [
    E(a),
    Not(B(a)),
    Or(Not(E(a)), B(a))
]

s = Solver()
for g in clauses:
    s.add(g)

print(s.check())
print(s.model() if s.check() == sat else "UNSAT")