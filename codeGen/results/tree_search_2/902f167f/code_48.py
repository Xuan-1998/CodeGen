import math

def min_squares(n, m):
    dp = {}

    def dfs(i, j):
        if (i, j) in dp:
            return dp[(i, j)]
        
        if i == 0 or j == 0:
            return 0
        
        res = float('inf')
        
        for k in range(1, int(math.sqrt(i)) + 1):
            for l in range(1, int(math.sqrt(j)) + 1):
                if i % k == 0 and j % l == 0:
                    res = min(res, dfs(i // k, j // l) + 1)
        
        dp[(i, j)] = res
        return res
    
    return dfs(n, m)

# Read input from stdin
n, m = map(int, input().split())

print(min_squares(n, m))
