def solve(a, b):
    MOD = 10**9 + 7
    d = {0: 0}
    res = 0

    for i in range(1, 316):
        if (b >> i) & 1:
            res = (res + d.get(b >> 1, a)) % MOD
        else:
            res = (res + d[b >> 1]) % MOD
        d[b] = (d.get(b >> 1, a) ^ b) % MOD

    return res
