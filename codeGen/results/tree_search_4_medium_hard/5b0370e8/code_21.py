def solve(k):
    MOD = 10**9 + 7
    dp = [[0] * (1 << k) for _ in range(20)]
    last_bit = [False] * 20

    def rec(i, and_mask, xor_mask):
        if i < 0:
            return 1
        res = 0
        for p in range(2**k):
            new_and_mask = and_mask | (p & ((1 << k) - 1))
            new_xor_mask = xor_mask ^ p
            if p & last_bit[i]:
                res += rec(i + 1, new_and_mask, new_xor_mask)
            else:
                res = (res + rec(i + 1, new_and_mask, new_xor_mask)) % MOD
        return res

    ans = 0
    for i in range(2**k):
        and_mask = xor_mask = 0
        for j in range(n):
            bit = ((i >> j) & 1)
            if bit:
                and_mask |= (1 << k - 1)
                xor_mask ^= (1 << k - 1)
            else:
                and_mask |= (p >> (k - 1))
                xor_mask ^= p
        ans = (ans + rec(n, and_mask, xor_mask)) % MOD

    return ans
