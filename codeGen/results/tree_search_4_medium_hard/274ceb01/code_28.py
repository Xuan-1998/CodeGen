import sys

n = int(input())
marks = list(map(int, input().split()))

dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = min(dp[j] + (i - j) for j in range(i))

print(min(dp))
