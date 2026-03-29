from collections import defaultdict

def min_operations(n, x):
    if len(str(x)) == n:
        return 0
    dp = [[-1] * (10**18 + 1) for _ in range(20)]
    memo = {}
    
    def dfs(i, j):
        if i < 0 or j < 0:
            return -1
        if len(str(j)) == i:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]
        
        res = float('inf')
        for k in range(10):
            new_j = j * 10 + k
            res = min(res, dfs(i-1, new_j))
        memo[(i, j)] = res + 1 if res != -1 else -1
        return memo[(i, j)]
    
    return dfs(n-1, x)

# Read input from standard input
n, x = map(int, input().split())
print(min_operations(n, x))
