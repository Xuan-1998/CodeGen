import sys

n = int(input())
dp = [0] * (n + 1)

for i in range(1, n + 1):
    a_i, b_i = map(int, input().split())
    dp[i] = max(dp[i-1], b_i - a_i)

print(min((i for i in range(n+1) if i > 0 and dp[i-1] < dp[i]), default=n))
