def count_paths(k, n, arr):
    dp = [[[0] * (k+1) for _ in range(n)] for _ in range(n)]
    dp[0][0][0] = 1
    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                for coin in range(arr[i-1][j-1]+1):
                    dp[i][j][coin] = dp[i-1][j][coin-arr[i-1][j-1]] if coin >= arr[i-1][j-1] else 0
            elif j == i:
                for coin in range(arr[i-1][i-1]+1):
                    dp[i][j][coin] = dp[i-1][j-1][coin-arr[i-1][i-1]] if coin >= arr[i-1][i-1] else 0
            else:
                for coin in range(arr[i-1][j-1]+1):
                    dp[i][j][coin] = dp[i-1][j][coin-arr[i-1][j-1]] if coin >= arr[i-1][j-1] else 0 + dp[i-1][j-1][coin-arr[i-1][j-1]] if coin >= arr[i-1][j-1] else 0
    return sum([dp[n-1][n-1][k]])

import sys
input = lambda: [int(i) for i in input().split()]
k, n = input()
arr = [[*map(int, input().split())] for _ in range(n)]
print(count_paths(k, n, arr))
