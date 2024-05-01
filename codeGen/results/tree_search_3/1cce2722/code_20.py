import sys

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for k in range(a[i-1], -1, -1):
            if i > 0 and k > 0:
                dp[i][k] = max(dp[i-1][j] - 1 for j in range(k+1))
            else:
                dp[i][k] = 0

    return max(dp[n])

print(solve())
