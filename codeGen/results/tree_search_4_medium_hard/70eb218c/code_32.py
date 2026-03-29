def min_operations(n, x):
    dp = [0] * (n + 1)
    dp[1] = len(str(x))

    def recursive_memoization(i):
        if i == 1:
            return dp[i]
        elif i > 1 and not memoized.get(i):
            min_ops = float('inf')
            for j in range(min(i-1, len(str(x))-1), i):
                ops = recursive_memoization(j) + (i - j - 1) + (x // 10**j != 0)
                if ops < min_ops:
                    min_ops = ops
            memoized[i] = min_ops
        return memoized.get(i, -1)

    memoized = {}
    for i in range(2, n+1):
        dp[i] = recursive_memoization(i)

    return dp[n]

n, x = map(int, input().split())
print(min_operations(n, x))
