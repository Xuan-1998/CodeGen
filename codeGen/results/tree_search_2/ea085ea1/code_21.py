import sys

N = int(input())

dp = [[[0 for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(i, N+1):
        for k in range(1, N+1):
            for l in range(k, N+1):
                if all(str1[i-1] == str2[l-1] or str1[i-1] == '*' and str2[l-1] != '@' or str1[i-1] == '@' and str2[l-1] == '*'):
                    dp[i][j][k] = max(dp[i][j][k], 1 + dp[i-1][j-1][k-1] if i > 0 and j > 0 and k > 0 else 0)

ans = 0
for i in range(N+1):
    for j in range(i, N+1):
        for k in range(N+1):
            for l in range(k, N+1):
                ans = max(ans, dp[i][j][k])

print(ans)
