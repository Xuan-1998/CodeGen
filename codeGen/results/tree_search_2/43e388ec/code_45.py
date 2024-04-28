import sys

MOD = 10**9 + 7

def solve(a, b):
    k = len(bin(a)) - 2
    dp = [[0] * (b + 1) for _ in range(k + 1)]

    for i in range(k + 1):
        for j in range(b + 1):
            if i == 0:
                dp[i][j] = a & b
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD

    ans = 0
    for i in range(k + 1):
        for j in range(b + 1):
            if i == k and j == b:
                continue
            ans = (ans + dp[i][j]) % MOD

    return ans

a, b = map(int, input().split())
print(solve(a, b))
