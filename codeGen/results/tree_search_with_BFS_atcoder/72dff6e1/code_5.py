MOD = 998244353
N = int(input())
A = list(map(int, input().split()))

dp = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
dp[0][0][0] = 1

for i in range(N):
    new_dp = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
    for j in range(i+1):
        for k in range(j+1):
            if dp[i][j][k] == 0:
                continue
            # case 1: add a new number
            new_dp[i+1][j+1][1] += dp[i][j][k]
            new_dp[i+1][j+1][1] %= MOD
            # case 2: repeat the last number
            if k+1 <= A[i]:
                new_dp[i+1][j][k+1] += dp[i][j][k]
                new_dp[i+1][j][k+1] %= MOD
            # case 3: repeat a number that is not the last one
            if j-k+1 > 0:
                new_dp[i+1][j][k] += dp[i][j][k] * (j-k+1)
                new_dp[i+1][j][k] %= MOD
    dp = new_dp

ans = sum(sum(dp[N][j][k] for k in range(A[j]+1)) for j in range(N))
print(ans % MOD)

