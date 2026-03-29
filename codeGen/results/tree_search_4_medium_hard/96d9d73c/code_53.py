def can_partition(A):
    N, K, M = A[0], A[1], A[2]
    A = [x for x in A[3:]]  # Remove the first three elements

    dp = [[False] * (K + 1) for _ in range(N + 1)]

    def can_add_to_partition(i, j):
        if i < K:
            return False
        if j > 0:
            return (A[i-1]-A[i-K]) <= M and i >= K
        return True

    dp[0][j] = False for all j > 1
    dp[i][0] is true only when i >= K

    for i in range(1, N + 1):
        for j in range(min(j+1, (i-1)//M+2), -1, -1):
            if can_add_to_partition(i, j):
                dp[i][j] = True
                break

    return dp[N][K]
