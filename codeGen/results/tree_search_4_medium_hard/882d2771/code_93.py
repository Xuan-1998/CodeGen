def f(r, k):
    memo = {}
    def dfs(r, k):
        if (r, k) in memo:
            return memo[(r, k)]
        
        if r == 0 or k == 0:
            return 0
        
        result = float('inf')
        for i in range(k + 1):
            result = min(result, f(r - i, k - 1) + i)
        
        memo[(r, k)] = result
        return result
    
    total = 0
    for i in range(t):
        total += dfs(r - i, t - i)
    
    return (total - l * f(r)) % (10**9 + 7)

t, l, r = map(int, input().split())
print(f(t, l, r))
