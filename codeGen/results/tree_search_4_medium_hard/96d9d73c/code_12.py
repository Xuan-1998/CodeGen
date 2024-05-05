def partition(A):
    N, K, M = map(int, input().split())
    dp = [[False] * (K + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, min(i, K) + 1):
            if j == 1:
                dp[i][j] = True
            else:
                for k in range(min(K, i - j), 0, -1):
                    if abs(A[i-1] - A[i-k]) <= M and dp[i-k][j-1]:
                        dp[i][j] = True
                        break

    return "Yes" if dp[N][K] else "No"
