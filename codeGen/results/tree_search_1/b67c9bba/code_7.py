from fractions import Fraction
from sys import stdin

# Function to calculate the expected number of shuffles for m elements
def expected_shuffles(m, memo):
    if m in memo:
        return memo[m]
    if m == 1:
        return Fraction(0)
    memo[m] = 1 + Fraction(m-1, m) * expected_shuffles(m-1, memo)
    return memo[m]

# Read the number of test cases
t = int(stdin.readline().strip())

# Precompute the expected number of shuffles for all possible values of n
memo = {}
for n in range(2, 151):
    expected_shuffles(n, memo)

# Process each test case
for _ in range(t):
    n = int(stdin.readline().strip())
    result = expected_shuffles(n, memo)
    # Output the result as an irreducible fraction
    print(f"{result.numerator}/{result.denominator}")
