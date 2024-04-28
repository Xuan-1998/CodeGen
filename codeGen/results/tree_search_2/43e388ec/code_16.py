def xor_sum(a, b):
    memo = {}
    def dfs(b, i):
        if (b, i) in memo:
            return memo[(b, i)]
        if b == 0:
            return 0
        result = dfs((b >> 1), i + 1)
        if (a & 1) ^ (b % 2):
            result += a
        return (result + ((10**9 + 7) - 1)) % (10**9 + 7)
    return sum(dfs(b, 0) for _ in range(314159))
