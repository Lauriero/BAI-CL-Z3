from z3 import *

def can_do_in(k):
    s = Solver()
    
    # Number of units of type 1 (4 weight units) for each trip i
    x = [Int(f"x_{i}") for i in range(k)]
    
    # Number of units of type 2 (3 weight units) for each trip i
    y = [Int(f"y_{i}") for i in range(k)]
    
    # Number of units of type 1 (1 weight units) for each trip i
    z = [Int(f"z_{i}") for i in range(k)]

    # For each trip
    for i in range(k):
        # We add carrying statements
        s.add(x[i] >= 0, y[i] >= 0, z[i] >= 0)

        # The weight should be lesser then 38 (50 (max weight) -12 (our weight))
        s.add(x[i] * 4 + y[i] * 2 + z[i] <= 38)

    # Condition that all sacks are transferred
    s.add(sum(x) == 40)
    s.add(sum(y) == 25)
    s.add(sum(z) == 20)

    return s.check(), s.model() if s.check() == sat else None


min_trips = 20

for i in range(1, 20):
    result, model = can_do_in(i)
    if result == sat:
        print('Minimum loaded trips: ', i)
        print(model)
        min_trips = i
        break

print('Minimum total trips: ', min_trips * 2 - 1)