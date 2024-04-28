def count_subarrays(arr, K):
    n = len(arr)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        max_val = arr[i - 1]
        for j in range(i, -1, -1):
            if arr[j - 1] > K:
                dp[i][j] = 1
            elif max(arr[j:i]) <= K:
                dp[i][j] = 0
            else:
                dp[i][j] = 1 if any(dp[k-1][j] for k in range(j, i)) else 0

    return sum(1 for x in dp[n])
