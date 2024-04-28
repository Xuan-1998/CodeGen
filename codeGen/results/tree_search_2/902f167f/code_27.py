from collections import defaultdict

def min_squares(n, m):
    memo = defaultdict(int)
    
    def dp(i, j):
        if i < 2 or j < 2:
            return 1
        
        key = (i, j)
        
        if memo[key] != 0:
            return memo[key]
        
        res = float('inf')
        for k in range(min(i, j)):
            res = min(res, dp(i-k-1, j) + dp(k, j-1))
        
        memo[key] = res
        return res
    
    return dp(n, m)

n, m = map(int, input().split())
print(min_squares(n, m))
