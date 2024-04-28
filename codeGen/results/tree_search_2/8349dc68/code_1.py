def max_sum_after_partitioning(arr, k):
    n = len(arr)
    dp = {}
    
    for i in range(k-1, -1, -1):  # start from the end of the array
        for j in range(1, min(i+2, k)+1):  # consider subarrays of length j
            if (i, j) not in dp:
                dp[(i, j)] = max(
                    dp.get((i-1, min(j, k)), arr[i]),  # considering the last element of previous subarray
                    dp.get((i-j+1, j-k+1), 0) + arr[i]  # considering all elements in current subarray
                )
    
    return max(sum(arr[i:i+j]) for (i, j) in dp.keys() if i >= k-1)
