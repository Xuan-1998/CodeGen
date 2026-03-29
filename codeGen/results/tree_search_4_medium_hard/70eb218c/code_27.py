===BEGIN CODE===
def min_operations(n, x):
    dp = [[0] * 10 for _ in range(n + 1)]

    # Base case: If the length of decimal representation of x is already i
    def helper(i, x):
        if len(str(x)) == i:
            return 0

        min_ops = float('inf')
        for y in range(1, 10):
            new_x = int(str(y) + str(x))
            ops = 1 + helper(i - 1, new_x)
            min_ops = min(min_ops, ops)

        return min_ops if min_ops < float('inf') else -1

    # Main function
    for i in range(1, n + 1):
        dp[i][int(str(x)[0])] = 1 + helper(i - 1, int(str(x)[0]))

    return dp[n][x]
