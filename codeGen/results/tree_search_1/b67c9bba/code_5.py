from fractions import Fraction

def expected_shuffles(n):
    dp = [Fraction(0)] * (n + 1)  # Using Fraction to handle exact arithmetic
    for i in range(2, n + 1):
        dp[i] = (i * dp[i - 1] + 1) / (i - 1)
    return dp[n]

# Reading the number of test cases
t = int(input().strip())

# Processing each test case
for _ in range(t):
    n = int(input().strip())
    result = expected_shuffles(n)
    # Printing the result as an irreducible fraction
    print(f"{result.numerator}/{result.denominator}")
