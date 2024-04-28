import sys

def xor_shift(a, b):
    memo = {}
    def dfs(b, i):
        if (b, i) in memo:
            return memo[(b, i)]
        if b == 0:
            return 0
        res = 0
        for j in range(i+1):
            res ^= a & ((1 << j) - 1)
        memo[(b, i)] = res % (10**9 + 7)
        return memo[(b, i)]
    ans = 0
    for _ in range(314159):
        b <<= 1
        if b > sys.maxsize:
            break
        a ^= b & ((1 << 20) - 1)
        ans += dfs(b, 0)
    print(ans % (10**9 + 7))
