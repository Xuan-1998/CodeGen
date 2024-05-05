def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(m + 1):
            if j == 0:
                dp[i][j] = f(gcd(*a[:i]))
            else:
                for k in range(i):
                    t = tuple(sorted([p for p in b[:j] if a[k:i].count(p)]))
                    if not t:
                        t = (0,)
                    dp[i][j] = max(dp[i][j], dp[k][min(j, m - 1)] + beauty(a[k:i], t))

    print(max(0, *dp[n]))

solve()
