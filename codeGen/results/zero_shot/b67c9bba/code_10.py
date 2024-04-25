from math import factorial
from fractions import Fraction

# Function to calculate the expected number of shuffles for improved bogosort
def expected_shuffles(n):
    # For n elements, the initial expectation is n!
    expectation = factorial(n)

    # For each element that gets fixed in its position, the number of
    # permutations for the remaining elements decreases.
    for i in range(1, n):
        expectation += factorial(n) / factorial(i)

    # Convert the result to an irreducible fraction
    result = Fraction(expectation, factorial(n)).limit_denominator()
    return result

# Main function to process input and output the results
def main():
    t = int(input().strip())  # Number of test cases
    for _ in range(t):
        n = int(input().strip())
        result = expected_shuffles(n)
        print(f"{result.numerator}/{result.denominator}")

if __name__ == "__main__":
    main()
