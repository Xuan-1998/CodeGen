from math import factorial
from fractions import Fraction

def expected_shuffles(n):
    # For n elements, the expected number of shuffles is n! (factorial of n)
    # since we only shuffle elements not in the correct position.
    return factorial(n)

def reduce_fraction(num, den):
    # Reduce the fraction num/den to its simplest form
    common_factor = Fraction(num, den)
    return common_factor.numerator, common_factor.denominator

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    n = int(input())
    
    # If n is 2 or more, calculate the expected number of shuffles
    if n >= 2:
        num, den = reduce_fraction(expected_shuffles(n), factorial(n))
        print(f"{num}/{den}")
    else:
        # If n is 1, no shuffles are needed as the sequence is already sorted
        print("0/1")
