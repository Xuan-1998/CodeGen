mod = 998244353
N = int(input())
A = list(map(int, input().split()))
A = [0] + A
dp = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
dp[0][0][0] = 1
for i in range(N):
    dpn = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
    for j in range(i+1):
        for k in range(j+1):
            if dp[i][j][k]:
                dpn[i+1][j][k] = (dpn[i+1][j][k] + dp[i][j][k]*(j-k)) % mod
                dpn[i+1][j][j] = (dpn[i+1][j][j] + dp[i][j][k]*(A[i+1]-j)) % mod
                dpn[i+1][j+1][k] = (dpn[i+1][j+1][k] + dp[i][j][k]*k) % mod
                dpn[i+1][j+1][j+1] = (dpn[i+1][j+1][j+1] + dp[i][j][k]*(A[i+1]-j)) % mod
    dp = dpn
print(sum(sum(dp[N][j]) for j in range(N+1)) % mod)

