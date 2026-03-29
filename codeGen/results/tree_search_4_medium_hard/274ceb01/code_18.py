import sys

n = int(input())
marks = list(map(int, input().split()))

dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = dp[i-1] - marks[i-1]

print(dp[n])
