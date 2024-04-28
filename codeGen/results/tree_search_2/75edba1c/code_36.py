def count_subarrays(N, K, Arr):
    # Initialize dp array
    dp = [[0] * (K + 1) for _ in range(N)]

    max_val = 0
    for i in range(N):
        max_val = max(max_val, Arr[i])
        for k in range(K, -1, -1):
            if Arr[i] > k:
                dp[i][k] = dp[i-1][k] + 1 if i > 0 else 1
            else:
                dp[i][k] = dp[i-1][k]
        max_val = 0

    total_subarrays = sum(dp[-1])
    return total_subarrays


N, K = map(int, input().split())
Arr = list(map(int, input().split()))

print(count_subarrays(N, K, Arr))
