def count_subarrays(Arr, K):
    N = len(Arr)
    dp = [[0] * (K + 1) for _ in range(N + 1)]

    count = 0
    max_val = 0

    for i in range(1, N + 1):
        max_val = max(max_val, Arr[i - 1])
        if max_val > K:
            count += 1
        for j in range(K + 1):
            dp[i][j] = dp[i - 1][j]
            if max_val > j:
                dp[i][j] += 1

    return count
