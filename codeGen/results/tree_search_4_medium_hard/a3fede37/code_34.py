def max_sum_of_path(arr):
    n = len(arr)
    memo = {i: arr[i] for i in range(n)}
    
    def dfs(i):
        if i >= n or memo[i] < 0:
            return memo[i]
        
        left_sum = dfs(2*i+1) if 2*i+1 < n else 0
        right_sum = dfs(2*i+2) if 2*i+2 < n else 0
        
        memo[i] = max(left_sum, right_sum) + arr[i]
        return memo[i]
    
    return max(dfs(i) for i in range(n))
