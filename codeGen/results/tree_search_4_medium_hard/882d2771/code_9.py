import sys

t, l, r = map(int, input().split())

dp = [[0] * (l-r+1) for _ in range(t)]

for i in range(1, t):
    dp[0][i-1] = 1 + min(dp[0][j] for j in range(i))

for i in range(l, r+1):
    for j in range(min(i, l), max(i, r)+1):
        if i == l:
            dp[i-j][0] = 1
        else:
            dp[i-j][0] = 1 + min(dp[m][i-1-m] for m in range(l, j))

ans = sum(t*(dp[l-i][0] - l) for i in range(r+1)) % (10**9 + 7)
print(ans)
