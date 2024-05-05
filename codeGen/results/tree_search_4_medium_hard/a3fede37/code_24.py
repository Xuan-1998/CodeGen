def max_sum_path(root):
    n = len(root) - 1
    dp = {i: val for i, val in enumerate(root)}
    
    for i in range(n//2):
        left = 2*i + 1
        right = 2*i + 2
        
        if root[left] and root[right]:
            dp[i] = max(dp[left], dp[right]) + root[i]
    
    return max(dp.values())
