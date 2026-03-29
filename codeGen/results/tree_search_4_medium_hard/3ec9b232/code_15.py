import sys

n = int(input())
M = list(map(int, input().split()))

# Initialize dp array with base case values
dp = [[0] * (1 << n) for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = 1

for i in range(1, n + 1):
    for p in range(1 << n):
        if not ((p >> M[i - 1]) & 1):  # Check if M[i-1] is included in the partition
            dp[i][p] = (dp[i][p] + dp[i - 1][p]) % (10**9 + 7)

print(dp[n][-1])
