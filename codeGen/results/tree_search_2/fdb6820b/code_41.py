import sys

# Read input from standard input
m, N = map(int, input().split())
arr = list(map(int, input().split()))

# Initialize dp array with base case
dp = [0] * (N + 1)
dp[0] = 1

for i in range(1, N + 1):
    for num in arr:
        if i >= num:
            dp[i] += dp[i - num]

print(dp[N] % (10**9 + 7))
