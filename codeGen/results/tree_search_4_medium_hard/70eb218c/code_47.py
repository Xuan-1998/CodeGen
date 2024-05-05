def min_ops(n, x):
    memo = {}
    dp = [float('inf')] * (n + 1)

    def helper(x):
        if x in memo:
            return memo[x]
        if len(str(x)) == n:
            return 0
        min_ops = float('inf')
        for d in range(10):
            new_x = d * 10 ** (len(str(x))) + int(x / 10)
            ops = helper(new_x) + 1
            min_ops = min(min_ops, ops)
        memo[x] = min_ops
        return min_ops

    dp[0] = 0
    for i in range(1, n + 1):
        x = int('1' * (10 ** (i - 1)) + '0')
        while x < 10 ** (i - 1):
            x *= 10
        dp[i] = helper(x)

    return dp[n]

if __name__ == '__main__':
    n, x = map(int, input().split())
    print(min_ops(n, x))
