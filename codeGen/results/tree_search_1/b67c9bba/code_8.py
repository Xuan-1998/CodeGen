from math import factorial
from fractions import Fraction

def expected_shuffles(m):
    if m == 0:
        return Fraction(0)
    return Fraction(1, 1 - Fraction(1, factorial(m)))

def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        result = expected_shuffles(n)
        print(f"{result.numerator}/{result.denominator}")

if __name__ == "__main__":
    main()
