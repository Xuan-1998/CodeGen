import sys
from math import prod

def calculate_probability(n, P, A, B):
    # Calculate probability of correctly numbering each ticket
    prob_individual = [p * (1 - p) for p in P]
    
    # Adjust based on whether all numbers are distinct
    if len(set(A + B)) == n:
        return prod(prob_individual)
    else:
        return 0

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    P = [float(x) for x in sys.stdin.readline().split()]
    A = [int(x) for x in sys.stdin.readline().split()]
    B = [int(x) for x in sys.stdin.readline().split()]
    result = calculate_probability(n, P, A, B)
    print(result)
