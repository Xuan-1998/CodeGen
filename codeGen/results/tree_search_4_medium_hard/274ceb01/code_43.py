import sys

n = int(input())
marks = list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = float('inf')
    for j in range(i):
        dp[i] = min(dp[i], dp[j] + (i - j) * marks[j])

print(dp[n])
