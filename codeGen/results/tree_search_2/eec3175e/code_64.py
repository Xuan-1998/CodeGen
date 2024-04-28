def can_sum_divisible_by_m(n, m, arr):
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    # Base case: sum 0 is always achievable
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if arr[i - 1] <= j:
                # If the current element is less than or equal to j,
                # we can either include it or not
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
            else:
                # The current element is more than j, so we can't include it
                dp[i][j] = dp[i - 1][j]

    return dp[n][m]


n = int(input())
m = int(input())
arr = list(map(int, input().split()))

print(can_sum_divisible_by_m(n, m, arr))
