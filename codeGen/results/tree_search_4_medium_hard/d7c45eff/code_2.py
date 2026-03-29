import sys

n, k = map(int, input().split())
s = input()

dp = [[[] for _ in range(k+1)] for _ in range(n+1)]

for i in range(n+1):
    dp[i][0] = ['' if i == 0 else s[:i]]

for j in range(k+1):
    if j > 0:
        dp[0][j] = [s[:j]]

for i in range(1, n+1):
    for j in range(min(i, k)+1):
        if j > 0 and len(s[j-1]) == 1:
            dp[i][j] = min(dp[i-1][max(j-1, 0)] + s[j-1], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][min(j, i)]

print(min(dp[n][k], key=len))
