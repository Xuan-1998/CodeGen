def solve():
    dp = {}
    a, b = map(int, input().split())
    ans = 0
    MOD = 10**9 + 7

    def func(i, a):
        if (i, a) in dp:
            return dp[(i, a)]
        if i > 314159:
            return 0
        b_shifted = b << i
        res = a ^ b_shifted
        dp[(i, a)] = res % MOD
        return res

    for _ in range(315):
        ans += func(_, a)
        a <<= 1
    print(ans % MOD)

if __name__ == "__main__":
    solve()
