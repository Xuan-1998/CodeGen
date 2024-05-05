from sys import stdin

N, K, M = map(int, stdin.readline().split())
A = list(map(int, stdin.readline().split()))

dp = [[False] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(min(i/K, (M+1)/M), 0, -1):
        if i < K:
            dp[i][j] = False
        else:
            max_val = max(A[:i])
            min_val = min(A[:i])
            if abs(max_val - min_val) <= M:
                dp[i][j] = True

print(dp[N][1])
