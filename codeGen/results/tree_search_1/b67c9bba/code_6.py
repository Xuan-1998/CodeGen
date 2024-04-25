from math import factorial
from fractions import Fraction

# Calculate the expected shuffles using dynamic programming
def expected_shuffles(m, dp):
    if m == 0:
        return 0
    if dp[m] != -1:
        return dp[m]
    
    # Calculate the expected value recursively
    expected_value = Fraction(1)
    for i in range(1, m):
        expected_value += expected_shuffles(i, dp) * Fraction(1, factorial(m))
    
    expected_value *= factorial(m)
    expected_value /= (factorial(m) - 1)
    
    dp[m] = expected_value
    return expected_value

def main():
    # Read the number of test cases
    t = int(input())
    dp = [-1] * 151  # Initialize DP array with -1 for memoization
    
    # Process each test case
    for _ in range(t):
        n = int(input())
        result = expected_shuffles(n, dp)
        
        # Print the result as an irreducible fraction
        print(f"{result.numerator}/{result.denominator}")

if __name__ == "__main__":
    main()
