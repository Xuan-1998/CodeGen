from math import factorial
from fractions import Fraction

# Function to calculate the expected number of shuffles for n unsorted elements
def expected_shuffles(n):
    # The expected number of shuffles is n! for n unsorted elements
    return factorial(n)

# Function to reduce a fraction to its simplest form
def reduce_fraction(numerator, denominator):
    frac = Fraction(numerator, denominator)
    return frac.numerator, frac.denominator

# Main function to process the input and output the result
def main():
    t = int(input().strip())  # Number of test cases
    for _ in range(t):
        n = int(input().strip())  # Number of elements in the sequence
        numerator, denominator = reduce_fraction(expected_shuffles(n), 1)
        print(f"{numerator}/{denominator}")

if __name__ == "__main__":
    main()
