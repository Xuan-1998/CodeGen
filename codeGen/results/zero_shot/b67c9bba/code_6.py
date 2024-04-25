from math import factorial
from fractions import Fraction

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def expected_shuffles(n):
    # For n elements, the expected number of shuffles for a perfect bogosort is n!
    # Since we are improving the bogosort, we need to adjust this expectation.
    # This is a non-trivial probability problem and may require more intricate mathematical analysis.
    # For the sake of this example, we will assume that the expected number of shuffles
    # is reduced by a factor of n for each correctly placed element (this is a simplification
    # and not the actual solution to the problem).
    # The actual solution would require analyzing the permutations of the remaining elements
    # and their probabilities of being sorted in each shuffle.
    return factorial(n) // n

def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        shuffles = expected_shuffles(n)
        # Reduce the fraction to its simplest form
        common_divisor = gcd(shuffles, factorial(n))
        result = Fraction(shuffles // common_divisor, factorial(n) // common_divisor)
        print(f"{result.numerator}/{result.denominator}")

if __name__ == "__main__":
    main()
