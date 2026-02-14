from z3 import *

People = ["Bart", "Dave", "Rex", "Zoey"]

# We create an object with boolean constants for knights
Knights = {p: Bool(f"Knight_{p}") for p in People}

# Says function is just a transformation, if it is the knight the statement should hold
def says(p, statement):
    return Knights[p] == statement

base_clauses = [
    says("Bart", Or(And(Knights["Rex"], Knights["Dave"]), And(Not(Knights["Rex"]), Not(Knights["Dave"])))),
    says("Dave", Not(Knights["Zoey"])),
    says("Rex", Not(Knights["Bart"])),
    says("Zoey", And(Knights["Rex"], Not(Knights["Dave"])))
]

s = Solver()
for c in base_clauses:
    s.add(c)

# To check whether the person is a knight, we must add Not(Knight) to the clauses and check for UNSAT
def isKnight(p):
    s.push()
    s.add(Not(Knights[p]))
    result = s.check()
    s.pop()
    return result == unsat

for p in People:
    print(f'{p} is a {'knight' if isKnight(p) else 'knave'}')