code_block
from math import modf

t, l, r = map(int, input().split())
mod = 10**9 + 7

dp = [[0] * (r+1) for _ in range(r+1)]

for i in range(2, r+1):
    for j in range(i-1, -1, -1):
        for k in range(j+1, i+j):
            dp[i][j] = min(dp[i][j], dp[k-1][j-k+1] + 1)

ans = 0
for i in range(t):
    ans += (l+i) * dp[r-l+i][i] - l * dp[r-l][i]
ans %= mod

print(ans)
