import sys

def solve():
    n = int(input())
    a = [int(x) for x in input().split()]

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(2, n + 1):
        for j in range(i, n + 1):
            if a[j - 1] % i == 0:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = dp[i][j - 1]

    return sum([dp[i][n] for i in range(2, n + 1)]) % (10**9 + 7)

print(solve())
