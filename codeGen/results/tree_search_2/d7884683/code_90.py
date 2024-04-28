def max_partitions(arr):
    n = len(arr)
    
    memo = {}
    
    def helper(i, j, left_sum, right_sum):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i >= j:
            return 1
        
        if left_sum == right_sum:
            return 2 + helper(i+1, j-1, 0, 0)
        
        if left_sum > right_sum:
            return 1 + helper(i+1, j, left_sum - arr[i], right_sum + arr[i])
        else:
            return 1 + helper(i, j-1, left_sum + arr[j], right_sum - arr[j])
    
    return helper(0, n-1, sum(arr[:n//2]), -sum(arr[n//2+1:]))
