from z3 import *;

Knight = {p: Bool(f"Knight_{p}") for p in ["a", "b", "c"]}
Werewolf = {p: Bool(f"Werewolf_{p}") for p in ["a", "b", "c"]}

def says(p, proposition):
    return Knight[p] == proposition

num_knaves = Sum([If(Not(Knight[p]), 1, 0) for p in ["a","b","c"]])

stmt1 = says("a", Werewolf["c"])
stmt2 = says("b", Not(Werewolf["b"]))
stmt3 = says("c", num_knaves >= 2)

stmt_one_werewolf = Sum([If(Werewolf[p], 1, 0) for p in ["a", "b", "c"]]) == 1

s = Solver()
s.add(stmt1)
s.add(stmt2)
s.add(stmt3)
s.add(stmt_one_werewolf)

def isWolf(p):
    s.push()
    s.add(Werewolf[p])
    result = s.check()
    s.pop()
    return result == sat

for p in ["a", "b", "c"]:
    print(f"a is {('possibly a wolf' if isWolf(p) else 'not a wolf')}")