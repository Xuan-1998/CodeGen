def solve(t, l, r):
    memo = {0: 0}
    for n in range(l, r + 1):
        if n % 2 == 0:
            f_n = 0
        else:
            i = (n - 1) // 2
            f_n = min(memo.get(i, float('inf')) + memo.get(n - i - 1, float('inf')), memo.get(n - 1, float('inf')))
        memo[n] = f_n
    return sum(t * pow(10, i) * (memo.get(l + i, 0) - l) for i in range(t)) % (10**9 + 7)
