from fractions import Fraction

def calculate_expected_shuffles(n):
    # Initialize the expected shuffles for a sequence of length 1 as 0
    dp = [Fraction(0)] * (n + 1)
    # Start from a sequence of length 2 up to n
    for i in range(2, n + 1):
        # Calculate the expected shuffles using the recurrence relation
        dp[i] = 1 + (i - 1) / i * dp[i - 1]
    return dp[n]

# Read the number of test cases from stdin
t = int(input())

# Process each test case
for _ in range(t):
    n = int(input())
    expected_shuffles = calculate_expected_shuffles(n)
    # Output the result in the form of an irreducible fraction
    print(f"{expected_shuffles.numerator}/{expected_shuffles.denominator}")
