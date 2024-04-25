from fractions import Fraction
from sys import stdin, stdout

# Recursive function to calculate the expected number of shuffles
def expected_shuffles(i, n, memo):
    if i == n:
        return 0
    if memo[i] != -1:
        return memo[i]

    # Calculate the expected number of shuffles
    exp_shuffles = Fraction(1, n - i)
    for j in range(n):
        if i != j:
            exp_shuffles += Fraction(1, n - i) * expected_shuffles(j, n, memo)
    
    memo[i] = exp_shuffles
    return exp_shuffles

# Read the number of test cases
t = int(stdin.readline().strip())

# Process each test case
for _ in range(t):
    n = int(stdin.readline().strip())
    memo = [-1 for _ in range(n)]
    result = expected_shuffles(0, n, memo)
    
    # Output the result in irreducible fraction form
    stdout.write(f"{result.numerator}/{result.denominator}\n")
