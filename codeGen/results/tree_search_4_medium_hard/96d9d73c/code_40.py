def canPartition(A, N, K, M):
    memo = {}

    def dp(i, k):
        if (i, k) in memo:
            return memo[(i, k)]

        if i < 0 or k <= 0:
            return False

        if A[i] > M * k:
            return False

        result = True
        for j in range(k-1, -1, -1):
            if dp(i-j-1, j) and abs(A[i]-A[i-j]) <= M:
                result = True
                break

        memo[(i, k)] = result
        return result

    return dp(N-1, K)
