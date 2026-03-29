import sys

n = int(input())
marks = list(map(int, input().split()))

dp = [0] * (n + 1)
for i in range(1, n + 1):
    if i == 1:
        dp[i] = marks[0]
    else:
        dp[i] = min(dp[j-1] + (i - j) - marks[j-1] for j in range(1, i+1))

print(dp[n])
