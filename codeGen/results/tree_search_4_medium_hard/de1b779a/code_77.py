import sys

n, m, c0, d0 = map(int, input().split())
dp = [0] * (n + 1)

for _ in range(m):
    ai, bi, ci, di = map(int, input().split())
    
for i in range(n + 1):
    dp[i] = max(dp[i], dp[max(0, i-ci)] + di) if ci > 0 else dp[i]

print(dp[n])
