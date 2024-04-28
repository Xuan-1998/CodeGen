import sys; input = sys.stdin.readline
MOD = 10**9 + 7

def solve():
    a, b = [int(x) for x in input().split()]
    dp = [[0] * (b.bit_length() + 1) for _ in range(315)]

    def f(i, a):
        if i > 314159: return 0
        if dp[i][a] != -1: return dp[i][a]
        res = f(i+1, (a & ~(1 << b.bit_length() - 1)) | ((a >> 1) & 1))
        res += f(i+1, a >> 1)
        return res % MOD

    print(sum(f(0, a), f(0, b)) % MOD)

solve()
