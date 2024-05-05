def count_digit_ones(n):
    def dp(k, n):
        if k == 0 or n < 10**(k-1):
            return int('1' * k) if n >= 10**(k-1) else 0
        if (n, k) in memo:
            return memo[(n, k)]
        res = 0
        for i in range(int(str(n)[:k])-1, str(n)[:k]+2):
            res += dp(k-1, i)
        res += str(n)[k] == '1'
        memo[(n, k)] = res
        return res

    memo = {}
    return sum(dp(len(str(n)) - 1, i) for i in range(n + 1))
