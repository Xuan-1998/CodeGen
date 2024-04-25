from fractions import Fraction

# Function to compute the expected number of shuffles
def expected_shuffles(n):
    # Base case for n = 2
    if n == 2:
        return Fraction(2)

    # Check if result is already computed
    if n in memo:
        return memo[n]

    # Recurrence relation: E(n) = 1 + sum(i=2 to n) [E(i-1) / i]
    expected_value = 1
    for i in range(2, n + 1):
        expected_value += expected_shuffles(i - 1) / i

    # Store the result in the memoization dictionary
    memo[n] = expected_value
    return expected_value

# Read the number of test cases
t = int(input())

# Initialize a memoization dictionary
memo = {}

# Process each test case
for _ in range(t):
    n = int(input())
    result = expected_shuffles(n)
    # Output the result as an irreducible fraction
    print(f"{result.numerator}/{result.denominator}")
