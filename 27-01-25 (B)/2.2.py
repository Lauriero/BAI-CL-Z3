from z3 import *

Person = DeclareSort('Person')

a = Const("a", Person)

D = Function("D", Person, BoolSort())
O = Function("O", Person, BoolSort())
L = Function("L", Person, BoolSort())

clauses = [
    Or(Not(D(a)), L(a)),
    And(O(a), Not(L(a))),
    Or(Not(O(a)), D(a))
]

s = Solver()
for g in clauses:
    s.add(g)

print(s.check())
print(s.model() if s.check() == sat else "UNSAT")