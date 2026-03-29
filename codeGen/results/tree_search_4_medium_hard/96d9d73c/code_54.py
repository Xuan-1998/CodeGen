from sys import stdin

N, K, M = map(int, stdin.readline().split())
A = list(map(int, stdin.readline().split()))

dp = [[False] * (K + 1) for _ in range(N + 1)]

for i in range(K, N + 1):
    dp[i][0] = True
    if i >= K:
        max_val = max(A[i-K:i])
        min_val = min(A[i-K:i])
        for j in range(1, min(i // K + 1, K) + 1):
            if (max_val - min_val) <= M and dp[i-K][j-1]:
                dp[i][j] = True
            else:
                dp[i][j] = False

print(dp[N][K])
