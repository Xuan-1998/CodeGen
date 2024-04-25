from fractions import Fraction
from math import factorial

def expected_shuffles(n):
    # We start with the probability of 1 for 0 shuffles (initial state)
    expected = Fraction(0)
    # Calculate the sum of probabilities for each shuffle until sorted
    for k in range(1, n+1):
        # Probability of sorting with k elements not in the correct position
        prob = Fraction(1, factorial(k))
        # Add the probability times the number of shuffles to the expected value
        expected += prob
    return expected

def main():
    t = int(input().strip())  # Read number of test cases
    for _ in range(t):
        n = int(input().strip())  # Read n for each test case
        result = expected_shuffles(n)
        print(f"{result.numerator}/{result.denominator}")  # Output irreducible fraction

if __name__ == "__main__":
    main()
