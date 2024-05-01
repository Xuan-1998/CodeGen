import sys

def has_subset_sum_divisible_by_m(n, m, arr):
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    
    # Base cases: if sum is 0, it's always possible to get that sum.
    for i in range(n + 1):
        dp[i][0] = True
    
    # If sum is not divisible by m, there's no subset with that sum.
    for j in range(m + 1):
        if j % m != 0:
            dp[0][j] = False
    
    for i in range(1, n + 1):
        for j in range(m + 1):
            # If the current number is larger than the sum, we can't include it.
            if j >= arr[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                # We have two choices: either include the current number or not.
                dp[i][j] = dp[i - 1][j] or (dp[i - 1][j - arr[i - 1]] if j >= arr[i - 1] else False)
    
    return dp[n][m]

n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(has_subset_sum_divisible_by_m(n, m, arr))
