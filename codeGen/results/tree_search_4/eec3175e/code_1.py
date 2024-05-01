def find_subset_sum_divisible(n, m, arr):
    dp = [[False] * (m+1) for _ in range(n+1)]
    
    for i in range(n+1):
        dp[i][0] = True
    
    for j in range(m+1):
        if j % m == 0:
            dp[0][j] = True
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if arr[i-1] <= j*m/m:
                dp[i][j] = (dp[i-1][j] or dp[i-1][(j*m + arr[i-1]) % m])
            else:
                dp[i][j] = dp[i-1][j]
    
    return 1 if dp[n][m] else 0

# Example usage
n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(find_subset_sum_divisible(n, m, arr))
