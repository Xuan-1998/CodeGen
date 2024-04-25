from fractions import Fraction
import sys

def expected_shuffles(i, j, dp):
    if j == 0:
        return Fraction(0, 1)
    if dp[i][j] != -1:
        return dp[i][j]

    # Calculate the expected shuffles for the current state
    # The +1 accounts for the current shuffle
    exp_shuffles = Fraction(1, 1) + expected_shuffles(i, j - 1, dp) * (j / i)
    # We need to divide by the probability of picking an out-of-place element
    exp_shuffles /= (j / i)

    dp[i][j] = exp_shuffles
    return exp_shuffles

def main():
    # Read the number of test cases
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
        result = expected_shuffles(n, n, dp)
        # Print the result as an irreducible fraction
        print(f"{result.numerator}/{result.denominator}")

if __name__ == "__main__":
    main()
