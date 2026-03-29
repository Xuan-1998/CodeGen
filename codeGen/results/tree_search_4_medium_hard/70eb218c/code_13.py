def min_operations(n, x):
    if n == 1:
        return 0 if x != 0 else -1
    
    memo = {}
    
    def helper(k):
        if k in memo:
            return memo[k]
        
        d = int(str(x)[-1])
        
        if d == 0:
            memo[k] = -1
            return -1
        
        length_x = len(str(x))
        
        if length_x <= k:
            memo[k] = 0
            return 0
        
        memo[k] = 1 + helper(k-1)
        
        return memo[k]
    
    return helper(n)

n, x = map(int, input().split())
print(min_operations(n, x))
