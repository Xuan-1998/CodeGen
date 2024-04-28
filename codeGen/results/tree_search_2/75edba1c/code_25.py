def count_subarrays(arr, K):
    N = len(arr)
    dp = [0] * (N+1)
    max_seen = 0

    for i in range(N):
        if arr[i] > K:
            max_seen = arr[i]
        else:
            max_seen = 0
        dp[i+1] = dp[i] + (max_seen > K)

    return dp[N-1]

# Example usage
N, K = map(int, input().split())
arr = list(map(int, input().split()))
print(count_subarrays(arr, K))
