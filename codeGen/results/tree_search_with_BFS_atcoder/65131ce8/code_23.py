MOD = 998244353
N = int(input())
D = list(map(int, input().split()))

if D[0] != 1:
    print(0)
    exit()

cnt = [0]*(N+1)
for d in D:
    cnt[d] += 1

if cnt[0] != 1:
    print(0)
    exit()

dp = [[0]*(N+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(1, N):
    for j in range(i+1):
        dp[i][j] = dp[i-1][j]
        if j > 0:
            dp[i][j] += dp[i-1][j-1]
        dp[i][j] %= MOD

ans = 1
sumD = 0
for d in range(1, N):
    for _ in range(cnt[d]):
        ans *= dp[sumD+cnt[d-1]][cnt[d]]
        ans %= MOD
        sumD += cnt[d-1]

print(ans)

