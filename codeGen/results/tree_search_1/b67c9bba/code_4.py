from fractions import Fraction

# Function to calculate the expected number of shuffles for the first i elements
def expected_shuffles(n):
    dp = [Fraction(0)] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + Fraction(1, i - 1)
    return dp[n]

# Read the number of test cases
t = int(input().strip())

# Process each test case
for _ in range(t):
    n = int(input().strip())
    result = expected_shuffles(n)
    # Output the result as an irreducible fraction
    print(f"{result.numerator}/{result.denominator}")

