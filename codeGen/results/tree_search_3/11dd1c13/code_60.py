def minFallingPathSum(A):
    n = len(A)
    memo = {}

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == 0:
            return A[0][j]

        res = float('inf')
        for k in range(j+1):
            res = min(res, dp(i-1, k)*A[i][k])
        memo[(i, j)] = res + A[i][j]
        return memo[(i, j)]

    res = 0
    for j in range(len(A[0])):
        res = min(res, dp(n-1, j))
    
    return res
