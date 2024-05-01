from collections import defaultdict

def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    memo = defaultdict(int)

    def dfs(i, j):
        if i <= 0 or j <= 0:
            return 1
        if (i, j) in memo:
            return memo[(i, j)]
        
        min_squares = float('inf')
        for k in range(1, min(i, j) + 1):
            min_squares = min(min_squares, dfs(i - k, j - k) + 1)
        
        memo[(i, j)] = min_squares
        return min_squares
    
    return dfs(n, m)

n, m = map(int, input().split())
print(min_squares(n, m))
