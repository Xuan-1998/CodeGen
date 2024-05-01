code
from collections import deque

def count_paths_to_k_coins(arr):
    n = len(arr)
    k = int(input())

    dp = [[[0] * (k + 1) for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j] <= k:
                if i == 0 and j == 0:
                    dp[i][j][arr[i][j]] = 1
                else:
                    if i > 0:
                        dp[i][j][arr[i][j]] += dp[i-1][j][k-arr[i][j]]
                    if j > 0:
                        dp[i][j][arr[i][j]] += dp[i][j-1][k-arr[i][j]]

    return dp[n-1][n-1][k]

print(count_paths_to_k_coins([[int(x) for x in input().split()] for _ in range(int(input()))]))
