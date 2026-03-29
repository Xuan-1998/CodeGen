def minF(a, n, s):
    memo = {}

    def f(i, t):
        if i == n:
            return 0
        if (i, t) in memo:
            return memo[(i, t)]

        res = float('inf')
        for x in range(t // a[i] + 1):
            y = t // a[i] - x
            if (x - s) * (y - s) >= 0 and f(i + 1, t - x * a[i]) < res:
                res = x * a[i] + f(i + 1, t - x * a[i])

        memo[(i, t)] = res
        return res

    return f(0, sum(a))
