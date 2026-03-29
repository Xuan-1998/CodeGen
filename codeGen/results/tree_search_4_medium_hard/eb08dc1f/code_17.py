def count_blocks(n):
    mod = 998244353
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for k in range(min(i + 1, n + 1), 0, -1):
            for v in range(10):  # iterate over each possible digit value
                if k > 1:
                    dp[i][k] += dp[i - 1][k - 1]
                else:
                    dp[i][k] += 1

    return [dp[i][i] % mod for i in range(n + 1)]

n = int(input())
print(*count_blocks(n), sep=' ')
