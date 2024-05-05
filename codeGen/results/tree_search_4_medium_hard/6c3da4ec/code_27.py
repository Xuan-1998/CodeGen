from collections import defaultdict

def max_bitwise_or(n, s):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    memo = defaultdict(int)

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            for k in range(i - 1, j):
                or_val = int(s[k:j], 2)
                dp[i][j] = max(dp[i][j], memo[(i - 1, k)] | or_val)
                memo[(i, j)] = dp[i][j]

    return bin(max(memo.values()))[2:]
