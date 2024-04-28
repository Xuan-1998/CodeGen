def max_sum_after_partitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)
    
    for i in range(k, n + 1):
        dp[i] = sum(max(arr[j-k+1:j+1]) for j in range(i - k + 1))
    
    return max(dp)

# Example usage:
arr = list(map(int, input().split()))
k = int(input())
print(max_sum_after_partitioning(arr, k))
