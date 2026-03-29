import sys

def count_words(n, m):
    MOD = 10**8 + 7
    dp = [[0] * (m // 2 + 1) for _ in range(n)]
    
    for i in range(1, n):
        for j in range(min(i, m // 2), -1, -1):
            if i >= 2 * j:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % MOD
            else:
                dp[i][j] = dp[i-1][j]
    
    total = sum(dp[-1])
    return (total + MOD - 1) % MOD

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    print(count_words(n, m))
