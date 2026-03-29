import sys

n = int(input())
marks = list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(1, n + 1):
    if i == 1:
        dp[i] = marks[0]
    else:
        dp[i] = min(dp[i-1] + (n-i) - sum(marks[:i]), dp[i-1] + marks[i-1])

print(min(dp))
