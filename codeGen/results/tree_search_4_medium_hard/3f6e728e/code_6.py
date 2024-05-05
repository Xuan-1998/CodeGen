import sys

input()
n, m, c = map(int, input().split())
u = list(map(int, input().split()))
l = list(map(int, input().split()))

dp = [0] * (c + 1)
dp[0] = 1

for i in range(1, c + 1):
    for j in range(n):
        if u[j] >= i:
            dp[i] = (dp[i] + dp[i - 1]) % int(1e9) + 7
    for k in range(m):
        if l[k] >= i:
            dp[i] = (dp[i] + dp[max(i - 1, 0)]) % int(1e9) + 7

print(*dp, sep=' ')
