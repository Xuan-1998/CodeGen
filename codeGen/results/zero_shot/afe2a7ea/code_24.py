        import math

    n = int(input())

    mod = 998244353

    p = pow(2, n - 1, mod)
    ans = (p + p) % mod

    print(ans)
