import sys

# Read input
n = int(input())
M = list(map(int, input().split()))

# Initialize variables
dp = [0] * (n + 1)
dp[0] = 1

for i in range(1, n):
    for j in range(i):
        if M[j] > M[i]:
            dp[i] += dp[j]
    dp[i] %= (10**9 + 7)

print(dp[-1])
