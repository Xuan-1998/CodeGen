import sys
from math import prod

def calculate_probability():
    T = int(sys.stdin.readline())
    probabilities = []
    
    for _ in range(T):
        n = int(sys.stdin.readline())
        p = []
        
        for _ in range(n):
            A, B, P = map(float, sys.stdin.readline().split())
            p.append((A, B, P))
        
        # Calculate the probability of correct numbering
        prob_correct = prod(P_i for A, B, P_i in p)
        
        probabilities.append(prob_correct)
    
    # Print the results
    for prob in probabilities:
        print("%.6f" % prob)

calculate_probability()
