def solve(t, l, r):
    memo = {2: 1}
    def f(n, memo):
        if n in memo:
            return memo[n]
        if n <= 2:
            return 1
        memo[n] = 1 + f(n//2, memo)
        return memo[n]

    t0 = t * f(l, memo)
    for i in range(1, t):
        t1 = t - i
        l1 = l + i
        r1 = r
        t0 -= l * f(l1, memo)
        for j in range(i+1, t):
            t2 = t - j
            l2 = l1 + j
            r2 = r1
            t0 += (t1 * f(l2, memo) - l1 * f(r2, memo))
    return t0 % (10**9 + 7)

t, l, r = map(int, input().split())
print(solve(t, l, r))
