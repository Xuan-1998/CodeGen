from math import gcd
from functools import reduce
from sys import stdin, stdout

def lcm(x, y):
    return x * y // gcd(x, y)

def main():
    t = int(stdin.readline().strip())
    dp = [0] * 151  # Initialize the dynamic programming array
    dp[1] = (0, 1)  # The base case: 0 shuffles needed for a single element, represented as a fraction (numerator, denominator)

    # Calculate dp values for all possible n
    for i in range(2, 151):
        numerator = 0  # The numerator of the expected value
        denominator = 1  # The denominator of the expected value
        for j in range(1, i):
            numerator = numerator * dp[j][1] + dp[j][0] * denominator
            denominator *= dp[j][1]
            common_denominator = reduce(lcm, [denominator] + [dp[k][1] for k in range(1, j + 1)])
            numerator *= common_denominator // denominator
            numerator += common_denominator // dp[j][1] * dp[j][0]
            denominator = common_denominator

        # Add the current shuffle
        numerator += denominator * i
        common_gcd = gcd(numerator, denominator)
        dp[i] = (numerator // common_gcd, denominator // common_gcd)

    # Process each test case
    for _ in range(t):
        n = int(stdin.readline().strip())
        stdout.write(f"{dp[n][0]}/{dp[n][1]}\n")

if __name__ == "__main__":
    main()
