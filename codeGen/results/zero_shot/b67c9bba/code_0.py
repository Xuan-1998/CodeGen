from math import gcd
from functools import reduce
from sys import stdin, stdout

# Function to calculate the least common multiple of two numbers
def lcm(a, b):
    return a * b // gcd(a, b)

# Function to calculate the expected number of shuffles for a given n
def expected_shuffles(n):
    # The probability of sorting the sequence in one shuffle is the reciprocal of
    # the number of permutations of the unsorted elements.
    # Since the sequence is initially sorted, all elements are in the correct position.
    # Therefore, the expected number of shuffles is just n! (factorial of n).
    # We represent this as a fraction with the numerator being n! and the denominator being 1.
    numerator = reduce(lambda x, y: x * y, range(1, n + 1), 1)
    denominator = 1
    
    # Reduce the fraction to its irreducible form
    common_divisor = gcd(numerator, denominator)
    numerator //= common_divisor
    denominator //= common_divisor
    
    return numerator, denominator

# Read the number of test cases
t = int(stdin.readline().strip())

# Process each test case
for _ in range(t):
    n = int(stdin.readline().strip())
    numerator, denominator = expected_shuffles(n)
    stdout.write(f"{numerator}/{denominator}\n")
