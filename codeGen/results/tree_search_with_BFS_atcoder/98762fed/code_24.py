import sys
from math import comb

mod = 998244353
N, M = map(int, sys.stdin.readline().split())
dp = [[[0]*401 for _ in range(401)] for _ in range(401)]
dp[0][0][0] = 1
for i in range(M):
    for j in range(N+1):
        for k in range(j+1):
            dp[i][j][k] = dp[i][j-1][k]
            if k < j:
                dp[i][j][k] = (dp[i][j][k] + dp[i][j-1][k+1]) % mod
    if i < M-1:
        for j in range(N+1):
            for k in range(N+1):
                for l in range(k+1):
                    dp[i+1][k][l] = (dp[i+1][k][l] + dp[i][j][k] * comb(N, l) * pow(2, N*(M-i-1), mod)) % mod
ans = sum(sum(dp[M-1][j][k] for k in range(N+1)) for j in range(N+1)) % mod
print(ans)

