import sys

def count_blocks(n):
    MOD = 998244353
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, min(i + 1, n + 1)):
            if i < j:
                dp[i][j] = dp[i - 1][j]
            elif j == 1:
                dp[i][j] = 10 ** (i - 1)
            else:
                for k in range(10):
                    if k * 10 ** (i - j) <= 10 ** i - 1:
                        dp[i][j] += dp[i - j][min(j - 1, n - i + j)] % MOD
                        break

    return [dp[n][i] for i in range(1, n + 1)]

n = int(sys.stdin.readline())
print(*count_blocks(n), sep=' ')
