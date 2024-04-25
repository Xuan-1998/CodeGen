from math import factorial
from fractions import Fraction

# Function to calculate the expected number of shuffles for 'm' elements
def expected_shuffles(m, memo):
    if m <= 1:
        return 0
    if m in memo:
        return memo[m]
    
    # Calculate the expected number of shuffles for 'm' elements
    total = factorial(m)
    exp = Fraction(1, m)
    for k in range(1, m):
        exp += Fraction(expected_shuffles(m - k, memo), factorial(k))
    exp *= Fraction(m, m - 1)
    memo[m] = exp
    return exp

def main():
    # Read number of test cases
    t = int(input().strip())
    memo = {}
    for _ in range(t):
        n = int(input().strip())
        # Since all elements are unique and range from 1 to n, they are all initially misplaced
        result = expected_shuffles(n, memo)
        # Print the result as an irreducible fraction
        print(f"{result.numerator}/{result.denominator}")

if __name__ == "__main__":
    main()
