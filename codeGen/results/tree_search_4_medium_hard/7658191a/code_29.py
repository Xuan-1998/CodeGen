import sys

def process_input():
    t = int(input())
    for _ in range(t):
        n, k, z = map(int, input().split())
        arr = list(map(int, input().split()))
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(min(i, k) + 1):
                if j <= z:
                    dp[i][j] = max(dp[i-1][j-1] + arr[i-1], dp[i-1][j] + (i > 1 and arr[i-2]))
                else:
                    dp[i][j] = dp[i-1][j]
        print(max(dp[n][k], dp[n-1][k-1] + arr[n-1]))

process_input()
