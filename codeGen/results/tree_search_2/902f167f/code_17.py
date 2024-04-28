def min_squares(n, m):
    memo = {}
    
    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        res = 0
        for k in range(1, min(i, j) + 1):
            if i >= k and j >= k:
                res = min(res, dp(i - k, j - k) + 1)
        
        memo[(i, j)] = res
        return res
    
    return dp(n, m)

n, m = map(int, input().split())
print(min_squares(n, m))
