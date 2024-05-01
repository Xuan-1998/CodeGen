def max_sum_of_partitioned_array(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)
    
    for i in range(k - 1, n):
        subarray_max = max(arr[i-k+1:i+1])
        dp[i + 1] = max(dp[i] + subarray_max, 0)
        
    return max(dp)

# Example usage:
arr = list(map(int, input().split()))
k = int(input())
print(max_sum_of_partitioned_array(arr, k))
