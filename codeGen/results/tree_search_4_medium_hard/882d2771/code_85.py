def f(n):
    MOD = 10**9 + 7
    memo = {}
    
    def helper(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == 1:
            memo[(i, j)] = min(j - 1, n - 1)
        else:
            n_groups = (n + i - 1) // i
            max_girls_per_group = min(j, n_groups)
            
            memo[(i, j)] = helper(i + 1, max_girls_per_group)
        
        return memo[(i, j)]
    
    result = 0
    for t in range(t):
        if l == r:
            result += (l - 1) * f(l)
        else:
            result += (r - l + 1) * helper(2, r // 2)
    
    return int(result % MOD)

t, l, r = map(int, input().split())
print(f(t, l, r))
