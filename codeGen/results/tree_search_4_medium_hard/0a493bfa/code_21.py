import sys

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    dp = [[[0] * (m + 1) for _ in range(n + 1)] for _ in range(2)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i > 0 and j >= b[i - 1]:
                dp[1][j][i] = max(dp[1][j][i], dp[1][j - b[i - 1]][i - 1])
            else:
                dp[1][j][i] = dp[0][j][i]
        for j in range(n + 1):
            if i > 0 and a[j] % b[i - 1] == 0:
                dp[1][j][i] = max(dp[1][j][i], dp[0][j][i - 1])
        for i2 in range(i + 1):
            for j2 in range(j + 1):
                if i2 > 0 and b[i2 - 1] <= a[j2]:
                    dp[1][j2][i2] = max(dp[1][j2][i2], dp[0][j2][i2 - 1])
                    j2 -= (a[j2] // b[i2 - 1]) * (b[i2 - 1])

    return dp[1][-1][-1]

print(solve())
