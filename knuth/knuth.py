import math, sys
from decimal import Decimal
from typing import Final
from heapq import heappop, heappush

MAX_FACTORIAL: Final = 100000
FLR_PRIORITY: Final = 1
SQRT_PRIORITY: Final = 2
FACT_PRIORITY: Final = 3

#retriving argument from command line
arg1 = 100
if(len(sys.argv) > 1): arg1 = int(sys.argv[1])
else: print("Expected syntax is python3 knuth.py n  Since no n was detected using an n of 100")

# Knuth starts with the ineger 3, then successively takes its square root, floor, and factorial until
# it reaches the input value of n.  Using BFS but with a priority queue because taking square roots of very large factorial
# numbers is taking a long time (obviously), so putting factorial on the lowest priority.   
def knuth(n):
    kq = []
    front = (1, (3.0, "")) #each node has a priority, a value and a string representing its history.  The strings will be something like "!fsfs!""
    seen = [] #seen are the visited nodes
    heappush(kq, front) #heapq is one of python's priority queue implementations
    while front[1][0] != n and len(kq) > 0:
        front = heappop(kq)
        hist = front[1][1]
        val = front[1][0]
        if val == float("inf"): continue #sometimes the numbers are too large for floats and python just returns "inf"
        floor = math.floor(val)
        if val not in seen:
            heappush(kq, (FLR_PRIORITY, (math.floor(val), hist + "f"))) #f is for floor
            if (val < MAX_FACTORIAL and floor == val): heappush(kq, (FACT_PRIORITY, (math.factorial(int(val)), hist + "!"))) #! is for factorial
            if (val >= 3): heappush(kq, (SQRT_PRIORITY, (float(Decimal(val).sqrt()), hist + "s"))) #s is for sqrt
            seen.append(val)
    print(front[1][0])
    if (front[1][0] == n): return front[1][1]
    else: return "could not find"
print(knuth(arg1))




