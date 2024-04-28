def max_sum_after_partitioning(arr, k):
    n = len(arr)
    dp = {}
    
    for i in range(n):
        for j in range(1, min(i+1, k)+1):
            if i < j:
                dp[(i-j+1, j)] = max(dp.get((i-j+1, j-1), arr[i-j+1:j]) + arr[i], 
                                       dp.get((max(0, i-j-k+2), j)) or 0)
    
    return sum(dp.values())
