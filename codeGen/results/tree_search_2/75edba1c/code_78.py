def count_subarrays(Arr, K):
    n = len(Arr)
    dp = [0] * n
    dp[0] = 1

    for i in range(1, n):
        if max(Arr[i:]) > K:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = dp[i-1]

    return sum(dp)
