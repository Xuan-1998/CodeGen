from sys import stdin

N, K, M = map(int, stdin.readline().split())
A = list(map(int, stdin.readline().split()))

dp = [[False] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(min(i, K), 0, -1):
        if A[i-1] - M >= K:
            dp[i][j] = dp[i-1][j]
        elif A[i-1] + M < K:
            dp[i][j] = False
        else:
            min_val, max_val = A[i-1] - M, A[i-1] + M
            if min_val >= K:
                dp[i][j] = dp[i-1][j]
            elif max_val < K:
                dp[i][j] = False
            else:
                valid_partitions = sum((val - A[i-1]) // (2*M + 1) for val in A[:i-1])
                if j >= valid_partitions:
                    dp[i][j] = True

print(dp[N][K])
