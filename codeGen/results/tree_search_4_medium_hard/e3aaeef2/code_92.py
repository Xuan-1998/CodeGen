import sys

def dp(n, m):
    MOD = 10**9 + 7
    dp = [[0] * (m+1) for _ in range(n+1)]

    # base case: no operations
    for i in range(1, n+1):
        dp[i][0] = len(str(i))

    for k in range(1, m+1):
        for i in range(1, n+1):
            if i < 10:
                dp[i][k] = min(dp[i][k-1], 1)
            else:
                # apply operation to each digit
                for d in str(i)[::-1]:
                    dp[int(d), k] = min(dp[int(d), k-1], len(str(int(d)+1)))
                i = int(''.join(reversed(str(i))))
                dp[i][k] = min(dp[i][k-1], len(str(i)))

    return dp[n][m]

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(dp(n, m) % MOD)
