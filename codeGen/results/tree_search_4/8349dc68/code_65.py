import sys
from functools import lru_cache

def max_sum_after_partition(arr, k):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n)]

    @lru_cache(None)
    def dfs(i, j):
        if i > j:
            return 0
        if j == 0:
            return arr[i - 1]
        if dp[i][j]:
            return dp[i][j]

        max_sum = max(dfs(i, j - 1), arr[i - 1])
        for jj in range(1, min(i + 1, k) + 1):
            max_sum = max(max_sum, dfs(i - jj, j - jj) + arr[i - 1])

        dp[i][j] = max_sum
        return max_sum

    return dfs(n, k)

# Example usage:
arr = list(map(int, input().split()))
k = int(input())
print(max_sum_after_partition(arr, k))
