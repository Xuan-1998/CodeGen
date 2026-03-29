import sys

def longest_increasing_subsequences():
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i][j] = min(dp[i-1][k], dp[k][j]) + 1
            else:
                dp[i][j] = max(0, dp[i-1][j])
        for j in range(i+1, n + 1):
            if arr[j-1] < arr[i]:
                dp[i][j] = min(dp[i-1][k], dp[k][j]) + 1
            else:
                dp[i][j] = max(0, dp[i][j-1])

    max_length = max(max(row) for row in dp[:-1, :-1])
    print(max_length)

longest_increasing_subsequences()
