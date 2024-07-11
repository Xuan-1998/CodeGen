MOD = 998244353
N = int(input())
D = list(map(int, input().split()))
D = [0] + D
P = [0]*(N+1)
for i in range(2, N+1):
    P[i] = P[i-1] + D[i-1]
dp = [[0]*(N+1) for _ in range(N+1)]
dp[1][1] = 1
for i in range(2, N+1):
    for j in range(1, i+1):
        dp[i][j] = (dp[P[i]][j-1]*D[j]%MOD + dp[i-1][j]*j%MOD)%MOD
ans = sum(dp[i][1] for i in range(1, N+1))%MOD
print(ans)

