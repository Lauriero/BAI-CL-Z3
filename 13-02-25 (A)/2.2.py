from z3 import *

Person = DeclareSort('Person')
a = Const("a", Person)
b = Const("b", Person)

C = Function('C', Person, BoolSort())
M = Function('M', Person, BoolSort())

clauses = [
    C(a),
    Not(C(b)),
    Or(Not(C(a)), Not(M(a))),
    Or(Not(C(b)), Not(M(b))),
    Not(M(a)),
    Not(M(b))
]

s = Solver()
for g in clauses:
    s.add(g)

print(s.check())
print(s.model() if s.check() == sat else "UNSAT")
