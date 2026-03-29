def lis_length(arr):
    n = len(arr)
    memo = {}

    def dp(i):
        if i in memo:
            return memo[i]
        
        max_lis = 1
        for j in range(i):
            if arr[i] > arr[j]:
                max_lis = max(max_lis, dp(j) + 1)
        
        memo[i] = max_lis
        return max_lis
    
    return max(dp(i) for i in range(n))
