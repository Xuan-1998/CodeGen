def solve(t, l, r):
    MOD = 10**9 + 7

    # Calculate f(n) for n <= 2 directly
    f = [0] * (r + 1)
    f[1], f[2] = 1, 1

    # Memoize values computed during recursion to avoid redundant calculations and accelerate computation.
    memo = {}
    def calc_f(n):
        if n in memo:
            return memo[n]
        if n <= 2:
            return f[n]

        res = float('inf')
        for i in range(2, n+1):
            res = min(res, calc_f(i) + (n - i))
        memo[n] = res
        return res

    # Calculate the value of the expression t0·f(l) + t1·f(l + 1) + ... + tr - l·f(r)
    total = 0
    for i in range(t):
        total += calc_f(min(i+l, r)) * (r-i)

    return int((total - l*calc_f(r)) % MOD)
