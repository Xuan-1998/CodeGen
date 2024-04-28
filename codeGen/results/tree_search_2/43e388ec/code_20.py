def solve(a, b):
    memo = {}

    def dp(i):
        if (a & b) == 0:  # base case: LSB of a or b is zero
            return 0
        elif i > 314159:  # base case: iteration index exceeds limit
            return 0
        else:
            key = (a, b, i)
            if key in memo:
                return memo[key]

            result = (a ^ (b << i)) % (10**9 + 7)  # compute XOR operation

            memo[key] = result
            return result

    for i in range(315):
        a = ((a >> 1) | (dp(i) & 1))
        b = (b >> 1)

    return dp(0)
