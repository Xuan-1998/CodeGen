import sys
input = sys.stdin.readline
n = int(input())
dp = [[[float('inf')] for _ in range(200001)] for _ in range(2)]
for _ in range(n):
    s, *a = map(int, input().split())
    dp[0][s][False] = 0
    for i in range(len(a)):
        for j in range(s+1,a[i]+1):
            if i == 0:
                dp[1][j][True] = min(dp[1][j][True], -a[i])
            else:
                dp[1][j][False] = min(dp[1][j][False], -dp[0][j-a[i]][True] + a[i])
    res = float('inf')
    for j in range(s+1,a[-1]+1):
        res = min(res, dp[1][j][False] - j)
print(res)
