import sys

N, M, C = map(int, input().split())
dp = [[0] * (M+1) for _ in range(N+1)]

for j in range(M+1):
    dp[0][j] = 1

for i in range(1, N+1):
    for j in range(min(i,M)+1):
        if j < M:
            dp[i][j] = (dp[i-1][j] * (N-i+1) + dp[i-1][j+1] * (M-j)) % (10**9+7)
        else:
            dp[i][j] = dp[i-1][j] * (N-i+1) % (10**9+7)

for _ in range(C):
    print(dp[_[1:M+1]][M], end=' ')
print()
