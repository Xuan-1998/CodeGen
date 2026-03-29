def solve(n, m):
    memo = {}

    def helper(num, ops):
        if (num, ops) in memo:
            return memo[(num, ops)]

        if ops == 0:
            result = num
        else:
            next_num = 0
            for digit in str(num):
                next_num = next_num * 10 + (int(digit) + 1)
            result = helper(next_num, ops - 1)

        memo[(num, ops)] = result % (10**9 + 7)
        return memo[(num, ops)]

    if n == 0 or m == 0:
        return 0

    return helper(n, m)
