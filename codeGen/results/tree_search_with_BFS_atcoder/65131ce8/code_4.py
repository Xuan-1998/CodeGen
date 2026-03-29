MOD = 998244353
N = int(input())
D = list(map(int, input().split()))
 
if D[0] != 1:
    print(0)
    exit()
 
D = [0] + D
S = [0]*(N+1)
for i in range(1, N+1):
    S[i] = S[i-1] + D[i]
 
if S[N] != N:
    print(0)
    exit()
 
dp = [[0]*(N+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(1, N+1):
    for j in range(i+1):
        dp[i][j] = dp[S[i-1]][j]*D[i] % MOD
        if j:
            dp[i][j] = (dp[i][j] + dp[S[i-1]][j-1]*(D[i]-1)) % MOD
 
print(sum(dp[N]) % MOD)

