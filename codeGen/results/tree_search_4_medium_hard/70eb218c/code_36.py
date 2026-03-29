def min_operations(n, x):
    dp = [[float('inf')] * (10 ** (n - 1)) for _ in range(20)]
    for i in range(2, n + 1):
        for j in range(10 ** (i - 1), 10 ** i):
            if len(str(j)) == i:
                dp[i][j] = 0
            else:
                min_ops = float('inf')
                last_digit = int(str(j)[-1])
                for k in range(10):
                    if k != last_digit:
                        y = j * 10 + k
                        min_ops = min(min_ops, dp[i - 1][y] + (len(str(y)) > i))
                dp[i][j] = min_ops

    return dp[n][x] if dp[n][x] < float('inf') else -1

# Read input from stdin
n, x = map(int, input().split())

print(min_operations(n, x))
