import sys

def alien_words(n, m):
    MOD = 10**8 + 7
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        if 2 * i <= n:
            dp[i] = sum(dp[j - i] for j in range(i + 1, n + 1))
        else:
            dp[i] = sum(dp[j - i] for j in range(i + 1, n + 1)) + 1
    return pow(2, m, MOD) * (dp[n] % MOD)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(alien_words(n, m))
