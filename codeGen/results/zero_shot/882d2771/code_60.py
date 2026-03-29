def solve():
    t, l, r = map(int, input().split())
    f = lambda n: n * (n - 1) // 2
    res = sum(t[i] * f(l + i) for i in range(r - l + 1)) - l * f(r)
    print(res % (10**9 + 7))
