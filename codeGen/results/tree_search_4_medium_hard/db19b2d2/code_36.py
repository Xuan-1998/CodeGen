import math

n, m, h = map(int, input().split())
s = list(map(int, input().split()))
dp = [[0.0 for _ in range(n+1)] for _ in range(m+1)]

for i in range(1, m+1):
    dp[i][0] = 1.0

for i in range(1, m+1):
    for k in range(n+1):
        if k < s[h-1]:
            dp[i][k] = 0.0
        elif i == 1:
            dp[i][k] = (min(k, s[h-1]) - min(0, k-s[h-1])) / math.comb(n, k)
        else:
            for x in range(min(k+1, s[h-1])+1):
                dp[i][k] += dp[i-1][n-k+x-1] * (min(x, s[h-1]) - min(0, x-s[h-1])) / math.comb(n, k)

print(dp[m][n])
