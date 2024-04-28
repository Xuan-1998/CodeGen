def count_subarrays(arr, K):
    N = len(arr)
    dp = [0] * N
    prev_max = float('-inf')
    for i in range(N):
        if arr[i] > K and arr[i] > prev_max:
            dp[i] = 1 + (dp[i-1] if i else 0) if i > 0 else 1
        else:
            dp[i] = dp[i-1] if i > 0 else 0
        prev_max = max(prev_max, arr[i])
    return sum(dp)
