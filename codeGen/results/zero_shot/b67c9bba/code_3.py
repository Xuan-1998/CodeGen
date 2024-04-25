from math import factorial
from fractions import Fraction

def expected_shuffles(n):
    # Calculate the expected number of shuffles for n elements
    # Using the fact that the expected number of shuffles for bogosort is n!
    # and adjusting for elements already in the correct position.
    e_shuffles = 0
    for k in range(n):
        e_shuffles += Fraction(1, k+1)
    return e_shuffles * factorial(n)

def main():
    t = int(input().strip())  # Read the number of test cases
    for _ in range(t):
        n = int(input().strip())  # Read the number of elements for each test case
        result = expected_shuffles(n)
        # Output the result as an irreducible fraction
        print(f"{result.numerator}/{result.denominator}")

if __name__ == "__main__":
    main()
