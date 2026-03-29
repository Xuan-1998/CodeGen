def can_partition(A):
    N, K, M = len(A), 1, 10**9
    dp = [[False] * (K + 1) for _ in range(N + 1)]

    # Base cases
    for j in range(K + 1):
        dp[0][j] = True
    for i in range(1, N + 1):
        dp[i][0] = False

    for i in range(1, N + 1):
        for j in range(1, min(i, K) + 1):
            if A[i - 1] <= M and (dp[i - 1][j - 1] or dp[i - 1][j]):
                dp[i][j] = True
            else:
                dp[i][j] = False

    return dp[N][K]

# Example usage:
N, K, M = map(int, input().split())
A = list(map(int, input().split()))
print(can_partition(A))
