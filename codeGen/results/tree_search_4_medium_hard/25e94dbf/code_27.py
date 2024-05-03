def solve(commands, n):
    memo = {}

    def dp(i, k):
        if (i, k) in memo:
            return memo[(i, k)]

        if i == 0:
            return 0

        res = 0
        for d in range(2):
            if d == int(commands[i] == 'F'):
                res = max(res, dp(i-1, min(k, n)) + 1)
            else:
                res = max(res, dp(i-1, k))

        memo[(i, k)] = res
        return res

    return dp(len(commands) - 1, n)

