MOD = 998244353
N = int(input())
D = list(map(int, input().split()))
D = [0] + D
cnt = [0]*(N+1)
for i in range(1, N+1):
    cnt[D[i]] += 1
if D[1] != 0 or cnt[0] != 1:
    print(0)
    exit()
dp = [[[0]*2 for _ in range(N+1)] for _ in range(N+1)]
dp[1][1][1] = 1
sum_dp = [[0]*2 for _ in range(N+1)]
sum_dp[1][1] = 1
for i in range(2, N+1):
    for j in range(1, i+1):
        dp[i][j][0] = (dp[i-1][j][0] + dp[i-1][j][1]) % MOD
        dp[i][j][1] = dp[i-1][j-1][0] * cnt[i-1] % MOD
        if j-2 >= 0:
            dp[i][j][1] += dp[i-1][j-1][1] * cnt[i-1] % MOD
            dp[i][j][1] -= sum_dp[j-2][1] * cnt[i-1] % MOD
        dp[i][j][1] %= MOD
    for j in range(i+1):
        sum_dp[j][0] = (sum_dp[j][0] + dp[i][j][0]) % MOD
        sum_dp[j][1] = (sum_dp[j][1] + dp[i][j][1]) % MOD
print(sum(dp[N][j][1] for j in range(N+1)) % MOD)

