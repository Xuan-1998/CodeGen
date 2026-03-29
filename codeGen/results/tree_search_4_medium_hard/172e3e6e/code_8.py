import sys

def good_subsequences():
    n = int(input())
    a = [int(x) for x in input().split()]
    MOD = 10**9 + 7

    dp = [[0] * (6 + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for pre in range(min(i, 6), -1, -1):
            if a[i - 1] % pre == 0:
                dp[i][pre] = (dp[i - 1][pre] + dp[i - 1][pre - 1]) % MOD
            else:
                dp[i][pre] = dp[i - 1][pre]

    return dp[n][0]

print(good_subsequences())
