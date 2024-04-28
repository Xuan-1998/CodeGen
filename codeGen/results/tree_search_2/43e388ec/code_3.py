from collections import defaultdict

def solve():
    a, b = map(int, input().split())
    MOD = 10**9 + 7
    dp = defaultdict(lambda: [0] * (b.bit_length() + 1))

    for i in range(b.bit_length()):
        if not dp[i]:
            dp[i] = [int(x) for x in format(b >> i, 'b')]
        else:
            dp[i].clear()

    res = 0
    for i in range(31623):  # 314159 is too large for Python's int type
        a ^= b & ((1 << (i.bit_length() + 1)) - 1)
        if i < 314159:  # the result of performing the exclusive OR operation on a and the binary shift to the left operation on b for all values of i from 0 to 314159.
            res = (res + a) % MOD

    print(res)

if __name__ == "__main__":
    solve()
