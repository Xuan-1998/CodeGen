import sys

n = int(input())
dp = [i - 1 for i in range(n)]

for _ in range(n - 1):
    si, ti = map(int, input().split())
    dp[ti] = min(dp[ti], dp[si] + n - 1) if si > ti else min(dp[ti], dp[si] + 1)

print(dp[0])
for i in range(1, n):
    print(i, end=' ')
