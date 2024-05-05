def find_max_similarity_score():
    A, B = input().split(), input().split()
    
    m, n = len(A), len(B)
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    memo = {}
    
    def dfs(i, j):
        if i == 0 or j == 0:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]
        
        if A[i - 1] == B[j - 1]:
            dp[i][j] = 4 + dfs(i - 1, j - 1)
        else:
            dp[i][j] = max(4, dfs(i - 1, j), dfs(i, j - 1))
        
        memo[(i, j)] = dp[i][j]
        return dp[i][j]
    
    print(dfs(m, n))

find_max_similarity_score()
