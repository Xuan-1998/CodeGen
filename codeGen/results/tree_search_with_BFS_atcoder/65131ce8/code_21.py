MOD = 998244353
N = int(input().strip())
D = list(map(int, input().strip().split()))
if D[0] != 1:
    print(0)
    exit()

dp = [[0]*N for _ in range(N)]
dp[0][0] = 1
cnt = [0]*N
cnt[0] = 1

for i in range(1, N):
    dp[i] = dp[i-1][:]
    for j in range(i, 0, -1):
        dp[i][j] = (dp[i][j] + dp[i-1][j-1] * cnt[D[i]-1]) % MOD
    for j in range(i+1):
        dp[i][j] = (dp[i][j] + dp[i-1][j] * (cnt[0] - cnt[D[i]])) % MOD
    cnt[D[i]] += 1

print(sum(dp[-1][i]*cnt[i] for i in range(N)) % MOD)

