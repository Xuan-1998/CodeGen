def min_operations(n, x):
    if n == 1:
        return 0

    memo = {}

    def dfs(x, n):
        if (x, n) in memo:
            return memo[(x, n)]

        if x < 10 and n > 1:
            return n - 1

        min_ops = float('inf')

        for d in str(x)[::-1]:
            ops = dfs(int(d), n-1) + len(str(x)) - len(str(d))
            min_ops = min(min_ops, ops)

        memo[(x, n)] = min_ops
        return min_ops

    return dfs(x, n)

# Read the input from standard input
n, x = map(int, input().split())

print(min_operations(n, x))
