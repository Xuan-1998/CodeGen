def min_xor(A, B):
    dp = [[float('inf')] * (B+1) for _ in range(A+1)]
    
    def dfs(i, j):
        if i < 0 or j < 0:
            return float('inf')
        if i == 0 and j == 0:
            return 0
        if dp[i][j] != float('inf'):
            return dp[i][j]
        
        res = float('inf')
        if j > 0:
            res = min(res, dfs(i-j, j-1) + j)
        if i >= j and A-i <= B-j:
            res = min(res, dfs(i-j, j) + i)
        
        dp[i][j] = res
        return res
    
    x = dfs(A, B)
    
    if x == float('inf'):
        return -1
    else:
        y = A - x
        return f"{x} {y}"

A = int(input())
B = int(input())
print(min_xor(A, B))
