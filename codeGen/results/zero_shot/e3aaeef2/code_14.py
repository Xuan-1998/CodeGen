import sys

# Read input
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    # Initialize dp array
    dp = [0] * (m + 1)
    dp[0] = len(str(n))

    for i in range(1, m + 1):
        # Calculate the number of digits in the resulting number after applying i operations
        dp[i] = dp[i - 1] + sum((int(digit) + 1).digits().count('1') for digit in str(n))

    # Print the answer modulo 10^9+7
    print(dp[m] % (10**9 + 7))
