from sys import stdin

N, K, M = map(int, stdin.readline().split())
A = list(map(int, stdin.readline().split()))

dp = [[False] * (K + 1) for _ in range(N + 1)]

for i in range(K):
    dp[i][0] = False
dp[0][0] = True

for i in range(1, N + 1):
    for j in range(min(i, K), 0, -1):
        if A[i-1] <= M or (j >= K and A[i-K-1] - A[i-1] <= M):
            dp[i][j] = True
        else:
            dp[i][j] = dp[i-1][j-1]
    for j in range(K + 1):
        if not dp[i][j]:
            break

print(dp[-1][-1])
