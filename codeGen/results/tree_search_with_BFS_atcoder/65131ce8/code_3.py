mod = 998244353
N = int(input())
d = list(map(int, input().split()))
d = [0] + d
if d[1] != 1 or d[0] > 0:
    print(0)
    exit()
dp = [[0]*(N+1) for _ in range(N+1)]
dp[1][1] = 1
cnt = [0]*(N+1)
cnt[1] = 1
for i in range(2, N+1):
    for j in range(1, i+1):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]*max(0, cnt[j]-d[i-1])) % mod
    cnt[i] = cnt[i-1] + d[i]
print(sum(dp[N]) % mod)

