import sys
from math import prod

def calculate_probability(n):
    # Initialize the probability of correct numbering
    correct_numbering_prob = 1
    
    for i in range(n):
        A_i, B_i, P_i = [int(x) for x in input().split()]
        
        # Calculate the probability that this ticket does not have a duplicate number
        prob_no_duplicate = (P_i / 100) * ((100 - P_i) / 99)
        
        # Update the correct numbering probability
        correct_numbering_prob *= prob_no_duplicate
    
    return 1 - correct_numbering_prob

T = int(input())
for _ in range(T):
    n = int(input())
    print("{:.6f}".format(calculate_probability(n)))
