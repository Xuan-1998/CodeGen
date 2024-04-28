def can_sum_divisible_by_m(n, m, arr):
    dp = [[False] * (m+1) for _ in range(n+1)]
    dp[0][0] = True  # base case: an empty subset has sum 0, which is divisible by any m

    for i in range(1, n+1):
        for j in range(1, m+1):
            if arr[i-1] % m == 0 and (j - arr[i-1]) >= 0 and dp[(i-1)][(j-arr[i-1])] is True:
                dp[i][j] = True
            elif dp[i-1][j]:
                dp[i][j] = True

    return dp[n][m]

# Example usage
n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(can_sum_divisible_by_m(n, m, arr))
