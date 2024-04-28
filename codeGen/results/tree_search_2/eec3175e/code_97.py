def can_sum_divisible(m, arr):
    n = len(arr)
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    
    # Base case: empty subset has sum 0
    dp[0][0] = True
    
    for i in range(1, n + 1):
        for j in range(m + 1):
            if j >= arr[i-1]:
                dp[i][j] = (dp[i-1][j] or dp[i-1][j-arr[i-1]])
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[n][m]

m, n = map(int, input().split())
arr = list(map(int, input().split()))
print(can_sum_divisible(m, arr))
