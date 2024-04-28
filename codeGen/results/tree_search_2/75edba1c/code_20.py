def count_subarrays(arr, K):
    n = len(arr)
    dp = [0] * (n + 1)
    dp[0] = 1

    max_prefix_sum = [0] * (n + 1)

    for i in range(n):
        max_prefix_sum[i + 1] = max(max_prefix_sum[i], arr[i])
        
    for i in range(1, n + 1):
        if max_prefix_sum[i] > K:
            dp[i] = dp[i - 1] + (i - max_prefix_sum.index(max_prefix_sum[i]) + 1)
    
    return dp[-1]

# Example usage
N = int(input())
K = int(input())
arr = list(map(int, input().split()))
print(count_subarrays(arr, K))
