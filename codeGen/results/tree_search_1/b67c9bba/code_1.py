from fractions import Fraction
from sys import stdin

# Recursive function to calculate expected shuffles
def expected_shuffles(n, k, memo):
    if k == 0:
        return 0
    if k == 1:
        return 1
    if (n, k) in memo:
        return memo[(n, k)]

    # Calculate the expected number of shuffles recursively
    expect = Fraction(1) + Fraction(1, k) * expected_shuffles(n, k - 1, memo) + \
             Fraction(k - 1, k) * expected_shuffles(n - 1, k - 1, memo)
    memo[(n, k)] = expect
    return expect

# Main function to handle multiple test cases
def main():
    t = int(stdin.readline().strip())  # Read the number of test cases
    for _ in range(t):
        n = int(stdin.readline().strip())  # Read the number of elements
        memo = {}
        result = expected_shuffles(n, n, memo)
        print(f"{result.numerator}/{result.denominator}")

# Run the main function
if __name__ == "__main__":
    main()
