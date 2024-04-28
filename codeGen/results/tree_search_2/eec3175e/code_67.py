def can_sum_divisible_by_m(arr, m):
    n = len(arr)
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if arr[i - 1] % m == 0:
                dp[i][j] = dp[i - 1][j]
            elif dp[i - 1][j]:
                dp[i][j] = True
            else:
                for k in range(j // m, j):
                    if dp[i - 1][k]:
                        dp[i][j] = True
                        break

    return dp[n][m]

# Example usage:
n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(can_sum_divisible_by_m(arr, m))
