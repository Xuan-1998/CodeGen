import sys

def solve():
    n = int(input())

    MOD = 998244353

    dp = [[False] * (n + 2) for _ in range(n + 2)]

    dp[0][0] = True

    for i in range(1, n + 2):
        for k in range(i + 1):
            if i == n + 1:
                dp[i][k] = False
            elif k > 0 and (dp[i-1][k-1] or dp[i-1][k]):
                dp[i][k] = True

    ans = 0
    for k in range(n + 2):
        if dp[n+1][k]:
            ans += 1
    print(ans % MOD)

solve()
