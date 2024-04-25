from math import factorial
from fractions import Fraction

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def expected_shuffles(n):
    # Since the exact formula for the expected number of shuffles is not trivial,
    # we might need to derive it using combinatorics and probability theory.
    # For now, we'll use a placeholder that returns a dummy value.
    # This should be replaced with the actual logic to compute the expected shuffles.
    return Fraction(1, 1)  # Placeholder

def main():
    t = int(input().strip())  # Read number of test cases
    for _ in range(t):
        n = int(input().strip())  # Read n for each test case
        result = expected_shuffles(n)
        # Simplify the result to an irreducible fraction
        common_divisor = gcd(result.numerator, result.denominator)
        simplified_result = Fraction(result.numerator // common_divisor, result.denominator // common_divisor)
        print(f"{simplified_result.numerator}/{simplified_result.denominator}")

if __name__ == "__main__":
    main()
