from math import factorial
from fractions import Fraction

def expected_shuffles(n):
    # For the sequence of n numbers, the probability of sorting in one shuffle is 1/n!
    # Expected shuffles = 1/probability = n!
    return factorial(n)

def main():
    t = int(input().strip())  # Number of test cases
    for _ in range(t):
        n = int(input().strip())  # Number of elements in the sequence
        exp_shuffles = expected_shuffles(n)
        # Convert to irreducible fraction
        fraction = Fraction(1, exp_shuffles).limit_denominator()
        print(f"{fraction.numerator}/{fraction.denominator}")

if __name__ == "__main__":
    main()
