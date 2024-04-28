def count_subarrays(N, K, Arr):
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    
    for i in range(1, N + 1):
        prev_max = max(Arr[:i])
        if prev_max > K:
            for j in range(K + 1):
                if prev_max > j:
                    dp[i][j] = dp[i - 1][j] + (prev_max > j)
                else:
                    dp[i][j] = dp[i - 1][j]
        else:
            for j in range(K + 1):
                dp[i][j] = dp[i - 1][j]
    
    return sum(dp[-1])

N, K = map(int, input().split())
Arr = list(map(int, input().split()))
print(count_subarrays(N, K, Arr))
