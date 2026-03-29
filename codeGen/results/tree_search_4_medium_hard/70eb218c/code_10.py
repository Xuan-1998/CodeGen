def dp(x, n):
    memo = {}

    def helper(x, n):
        if (x, n) in memo:
            return memo[(x, n)]

        if len(str(x)) == n:
            return 0

        last_digit = x % 10
        if last_digit != 0:
            op = 1 + helper(10*x // 10, n-1)
        elif n > 1:
            op = 1 + helper(x // 10, n-1)

        memo[(x, n)] = op
        return op

    return helper(x, n)

while True:
    n, x = map(int, input().split())
    if n < 2 or x >= 10**18:
        break
    print(dp(x, n))
