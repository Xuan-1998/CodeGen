import sys
K, N = map(int, input().split())
dp = [[[0]*(K+1) for _ in range(N)] for _ in range(N)]
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        dp[i][j][0] = 1
        if i > 0:
            dp[i][j][0] += dp[i-1][j][0]
        if j > 0:
            dp[i][j][0] += dp[i][j-1][0]
print(sum(sum(row[:K+1]) for row in dp[-1]))
