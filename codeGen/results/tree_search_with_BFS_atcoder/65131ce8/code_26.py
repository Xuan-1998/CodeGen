mod = 998244353
N = int(input())
d = list(map(int, input().split()))
d = [0] + d

dp = [[[0]*2 for _ in range(N+1)] for _ in range(N+1)]
dp[1][1][1] = 1

for i in range(2, N+1):
    for j in range(1, i+1):
        dp[i][j][0] = (dp[i-1][j][0] * (d[i] - j + 1) + dp[i-1][j-1][1] * (j - 1)) % mod
        dp[i][j][1] = (dp[i-1][j-1][0] + dp[i-1][j-1][1]) % mod

res = 0
for j in range(1, N+1):
    res = (res + dp[N][j][1]) % mod

print(res)

