from math import factorial
from fractions import Fraction

# Function to initialize the DP table
def initialize_dp(n):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 0  # If there are no elements out of place, no shuffles are needed
    return dp

# Function to calculate the expected number of shuffles
def calculate_expected_shuffles(n):
    dp = initialize_dp(n)
    
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            # Calculate the expected shuffles for a subsequence of length i with j elements out of place
            total_permutations = factorial(j)
            sorted_permutations = 0 if j != i else 1  # If all elements are out of place, there's no chance of sorting in one shuffle
            dp[i][j] = Fraction(total_permutations, total_permutations - sorted_permutations)
            for k in range(1, j):
                dp[i][j] += Fraction(factorial(j) - factorial(k), total_permutations - sorted_permutations) * dp[i][k]
            dp[i][j] = dp[i][j] / (1 - Fraction(sorted_permutations, total_permutations))
    
    return dp[n][n]

# Read number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    n = int(input())
    result = calculate_expected_shuffles(n)
    # Output the result as an irreducible fraction
    print(f"{result.numerator}/{result.denominator}")
