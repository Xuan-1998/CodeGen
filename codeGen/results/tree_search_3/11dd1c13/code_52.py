def minFallingPathSum(A):
    memo = {}
    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == 0:
            return A[0][j]
        res = float('inf')
        for k in range(j):
            res = min(res, dp(i-1, k)*A[i][k] + A[i][j])
        memo[(i, j)] = res
        return res

    n = len(A)
    return min(dp(n-1, j) for j in range(n))
