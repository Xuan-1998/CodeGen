import sys

def solve():
    n = int(input())  # Number of days
    marks = list(map(int, input().split()))  # Marks strictly above water on each day

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for k in range(1, min(i, marks[i - 1]) + 1):
            if k < marks[i - 1]:
                dp[i][k] = dp[i - 1][k]
            else:
                dp[i][k] = min(dp[i - 1][k], dp[i - 1][marks[i - 2]] + i - marks[i - 1])

    return dp[n][n]

print(solve())
