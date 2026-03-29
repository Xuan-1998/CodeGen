def solve():
    n = int(input())
    dp = [[False] * (n + 2) for _ in range(n + 2)]

    def or_(a: bool, b: bool) -> bool:
        return a or b

    def and_(a: bool, b: bool) -> bool:
        return a and b

    def any_(f):
        return any(f(x) for x in range(n + 1))

    dp[0][0] = True
    for i in range(1, n + 2):
        for j in range(min(i, n)):
            if or_(j <= i, and_(dp[i - 1][min(j + 1, i)], not_(any_(k in range(min(j + 1, i)), dp[i - 1][k])))):
                dp[i][j] = True

    print((1 if dp[n + 1][n] else 0) % 998244353)

solve()
