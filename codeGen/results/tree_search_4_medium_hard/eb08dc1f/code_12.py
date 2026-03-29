from collections import defaultdict

def count_blocks(n):
    MOD = 998244353
    dp = [[0] * (n + 1) for _ in range(10)]
    total_blocks = [0] * (n + 1)

    for i in range(10):
        dp[i][1] = 1

    for k in range(2, n + 1):
        for i in range(10):
            if k > 1:
                total_blocks[k-1] += dp[i][k-1]
                total_blocks[k-1] %= MOD
            for j in range(10):
                if i != j:
                    dp[j][k] += dp[i][k-1]
                    dp[j][k] %= MOD

    return ' '.join(map(str, [total_blocks[1]] + total_blocks[2:]))
