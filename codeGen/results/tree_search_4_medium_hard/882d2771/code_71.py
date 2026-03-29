def f(l, r):
    memo = {}
    
    def helper(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == j:
            return 0
        
        total = float('inf')
        
        for k in range(i, j+1):
            total = min(total, 1 + max(helper(i, k-1), helper(k+1, j)))
        
        memo[(i, j)] = total
        return total
    
    return sum(t * helper(l, l+t-1) for t in range(t)) - (l*(r-l))
