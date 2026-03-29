mod = 998244353
N = int(input())
d = list(map(int, input().split()))

if d[0] != 1:
    print(0)
    exit()

dp = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
dp[1][1][1] = 1

for i in range(1, N):
    for j in range(1, i+1):
        for k in range(1, i+1):
            if dp[i][j][k] > 0:
                dp[i+1][j+1][k+1] += dp[i][j][k]
                dp[i+1][j+1][k+1] %= mod
                dp[i+1][j][k+1] += dp[i][j][k]*((j+1 if j+1<=k else 0) + (k-j if k-j>=0 else 0))
                dp[i+1][j][k+1] %= mod

res = 0
for i in range(1, N+1):
    res += dp[N][d[N-1]][i]
    res %= mod

print(res)

