def max_sum(arr, k):
    n = len(arr)
    res = 0
    cur_max = float('-inf')
    
    for i in range(0, n, k):
        if i + k > n:
            break
        window_sum = sum(arr[i:i+k])
        cur_max = max(cur_max, max(arr[i:i+k]))
        res += cur_max
    
    return res
