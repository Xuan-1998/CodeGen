def beautycontest():
    t, l, r = map(int, input().split())
    mod = 10**9 + 7

    def f(n):
        if n == 1:
            return 0
        if n % 2 == 0:
            return 2 * f(n // 2)
        else:
            return 1 + min(f((n - 1) // 2), f((n + 1) // 2))

    res = t * f(l) + sum(t * f(i) for i in range(l + 1, r + 1)) - l * f(r)
    print(res % mod)

beautycontest()
