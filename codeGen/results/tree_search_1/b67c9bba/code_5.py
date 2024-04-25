from math import factorial
from fractions import Fraction
from sys import stdin, stdout

# Precompute factorials to avoid redundant calculations
factorials = [factorial(i) for i in range(151)]

def expected_shuffles(n):
    # Base case: If there are no misplaced elements, no shuffles are needed
    if n == 0:
        return Fraction(0, 1)
    
    # If there is one misplaced element, it's already in the correct position
    if n == 1:
        return Fraction(0, 1)
    
    # Calculate the expected number of shuffles for 'n' misplaced elements
    # This is the sum of 1 + (probability of not being sorted) * (expected shuffles for 'n' elements)
    exp_shuffles = Fraction(1, 1)
    exp_shuffles += Fraction(n - 1, factorials[n]) * expected_shuffles(n)
    return exp_shuffles

# Read the number of test cases from stdin
t = int(stdin.readline().strip())

# Process each test case
for _ in range(t):
    n = int(stdin.readline().strip())
    # Output the expected number of shuffles as an irreducible fraction
    stdout.write(f"{expected_shuffles(n).numerator}/{expected_shuffles(n).denominator}\n")
