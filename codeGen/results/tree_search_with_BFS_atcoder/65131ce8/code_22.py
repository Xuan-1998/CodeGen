import sys
input = sys.stdin.readline
mod = 998244353

N = int(input())
d = list(map(int, input().split()))
d = [0] + d
if d[1] != 1 or d[0] != 0:
    print(0)
    sys.exit()

dp = [[[0]*2 for _ in range(N+1)] for _ in range(N+1)]
dp[1][1][1] = 1
cnt = [0]*(N+1)
cnt[1] = 1

for i in range(2, N+1):
    dp[i][1][1] = dp[i-1][cnt[i-1]][0]
    dp[i][1][0] = dp[i-1][cnt[i-1]][1]
    cnt[i] = cnt[i-1] + d[i]
    for j in range(2, cnt[i]+1):
        dp[i][j][1] = (dp[i][j-1][1] + dp[i-1][j-1][0]) % mod
        dp[i][j][0] = (dp[i][j-1][0] + dp[i-1][j][1] + dp[i-1][j-1][0]) % mod

print(sum(dp[N][j][1] for j in range(1, cnt[N]+1)) % mod)

