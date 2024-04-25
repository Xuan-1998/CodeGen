from math import factorial
from fractions import Fraction

# Step 2: Calculate the probability of a sequence being sorted after a shuffle
def probability_sorted(n):
    # For a sequence of n numbers, there are n! permutations
    total_permutations = factorial(n)
    # Only one of these permutations is sorted
    return 1 / total_permutations

# Step 3: Determine the expected number of shuffles
def expected_shuffles(n):
    # The expected number of shuffles is the reciprocal of the probability
    return Fraction(1, probability_sorted(n)).limit_denominator()

# Step 4: Output the result as an irreducible fraction
def main():
    t = int(input().strip())  # Read the number of test cases
    for _ in range(t):
        n = int(input().strip())  # Read n for each test case
        result = expected_shuffles(n)
        print(f"{result.numerator}/{result.denominator}")  # Output as irreducible fraction

if __name__ == "__main__":
    main()
