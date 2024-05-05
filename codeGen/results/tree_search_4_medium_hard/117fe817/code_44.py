def countDigitOne(n):
    @functools.lru_cache(None)
    def dp(i):
        if i < 10:
            return int(str(i)[0] == '1')
        res = 0
        for d in range(1, 11):
            res += dp(i // 10) * (d < i % 10 or d > 1) + (i // 10 == d)
        return res

    return sum(dp(i) for i in range(n+1))

# Test the function
n = int(input())
print(countDigitOne(n))
