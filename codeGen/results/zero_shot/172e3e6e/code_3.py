import sys

def solve(n, a):
    MOD = 10**9 + 7
    dp = [[0] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(i, -1, -1):
            if a[j-1] % j == 0:
                dp[i][j] = (dp[i-1][j-1] + 1) % MOD
            else:
                dp[i][j] = dp[i-1][j]
    return sum(dp[n]) % MOD

n = int(input())
a = [int(x) for x in input().split()]
print(solve(n, a))
