from z3 import *

countries = ["GE", "AM", "AZ", "IR", "TR", "IQ"]

edges = [
    ("GE", "AM"), ("GE", "AZ"), ("GE", "TR"), 
    ("AM", "AZ"), ("AM", "IR"), ("AM", "TR"), 
    ("AZ", "IR"), ("AZ", "TR"), 
    ("IR", "TR"), ("IR", "IQ"), 
    ("TR", "IQ")
]

def can_color_with(k):
    s = Solver()
    color = {c: Int(c) for c in countries}
    for c in countries:
        s.add(color[c] >= 0)
        s.add(color[c] < k)

    for (a, b) in edges:
        s.add(color[a] != color[b])

    return s.check(), s.model() if s.check() == sat else None

res3, model3 = can_color_with(3) 
print("3-colorable:", res3)

res4, model4 = can_color_with(4) 
print("4-colorable:", res4) 
if res4 == sat: 
    print(model4)