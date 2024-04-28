def count_subarrays(N, K, arr):
    dp = [[0] * N for _ in range(N)]
    
    for i in range(N - 1, -1, -1):
        for j in range(i, N):
            if max(arr[i:j+1]) > K:
                dp[i][j] = (dp[i][j-1] + 1) if j < N - 1 else 1
            else:
                dp[i][j] = dp[i][j-1]
    
    return sum(dp[0])

N, K = map(int, input().split())
arr = list(map(int, input().split()))
print(count_subarrays(N, K, arr))
