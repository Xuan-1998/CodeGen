from math import factorial
from fractions import Fraction

# Function to calculate the expected number of shuffles for a subsequence of length k
def expected_shuffles(k):
    # Base case: if k is 1, no shuffles are needed
    if k == 1:
        return 0
    # Use the previously calculated expected value for subsequences of length k-1
    # and add the current step, which is k factorial (the number of permutations of k elements)
    return dp[k-1] + Fraction(1, factorial(k))

# Read the number of test cases
t = int(input())

# Precompute the expected shuffles for all possible subsequences up to 150
dp = [0] * 151
for i in range(2, 151):
    dp[i] = expected_shuffles(i)

# Process each test case
for _ in range(t):
    n = int(input())
    # Output the expected number of shuffles for a sequence of length n
    # as an irreducible fraction
    result = dp[n]
    print(f"{result.numerator}/{result.denominator}")
