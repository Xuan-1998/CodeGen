def solution():
    a, b = map(int, input().split())
    MOD = 10**9 + 7

    dp = {}
    for i in range(b.bit_length()):
        if (i, 0) not in dp:
            dp[(i, 0)] = a & 1
        else:
            dp[(i, 0)] = (dp[(i-1, 0)] + (a & 1)) % MOD

    res = 0
    for i in range(a.bit_length()):
        for j in range(b.bit_length()):
            if (j, i) not in dp:
                dp[(j, i)] = (dp.get((j-1, i), 0) + (a >> i) & 1 * (b >> j)) % MOD
    for _ in range(314159):
        res = (res + (dp.get((0, a.bit_length()-1), 0) + (a ^ (b << a.bit_length()))) % MOD)
    print(res)

solution()
