import sys
import math

def calculate_probability():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        probabilities = []
        for _ in range(n):
            A, B, P = map(float, sys.stdin.readline().split())
            probabilities.append((A, B, P))
        
        overall_probability = 1.0
        for A, B, P in probabilities:
            # Calculate the probability of choosing the correct number
            correct_number_probability = P * (1 - P)
            # Multiply the overall probability by this probability
            overall_probability *= correct_number_probability
        
        print(format(overall_probability, ".6f"))  # Round to 6 decimal places

calculate_probability()
