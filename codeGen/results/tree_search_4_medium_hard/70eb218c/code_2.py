def min_operations(n, x):
    dp = [[-1] * (len(str(x)) + 1) for _ in range(n + 1)]

    def recurse(k):
        if k == 0:  # impossible to make the length equal to n
            return -1
        if len(str(x)) <= k:  # no operation needed
            return 0

        min_ops = float('inf')
        for d in range(10):  # consider each digit from 0 to 9
            new_len = len(str(x * (10 ** (k - 1) + d)))
            if new_len <= n:  # update dp[i][j] only if the new length is less than or equal to i
                min_ops = min(min_ops, dp[new_len][new_len - k] + 1)
        return min_ops

    return recurse(n)

# Read input from stdin
n, x = map(int, input().split())

# Print the minimum number of operations to stdout
print(min_operations(n, x))
