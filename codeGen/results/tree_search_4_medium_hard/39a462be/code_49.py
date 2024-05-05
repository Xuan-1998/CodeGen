def maximal_similarity_score():
    n, m = [int(x) for x in input().split()]
    memo = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                memo[i][j] = memo[i - 1][j - 1] + 4
            else:
                memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])
    
    return memo[n][m]
