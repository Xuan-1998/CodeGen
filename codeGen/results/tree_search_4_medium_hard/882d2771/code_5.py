import sys

t, l, r = map(int, input().split())

dp = [[0] * (r + 1) for _ in range(l)]

for i in range(l):
    dp[i][i] = 1

for n in range(l, r + 1):
    for i in range(n - l + 1):
        min_comp = sys.maxsize
        for m in range(i, n + 1):
            min_comp = min(min_comp, dp[m - l][m])
        dp[i][n] = 1 + min_comp

ans = 0
for i in range(r + 1):
    ans += (t * dp[l - 1][i]) % (10**9 + 7)
print(ans)
