def solve():
    n, q = map(int, input().split())
    s = list(input())

    dp = [[[] for _ in range(q + 1)] for _ in range(n + 1)]

    def memo(i, j):
        if i == 0 or j == 0:
            return 0
        if dp[i][j]:
            return dp[i][j]

        res = float('inf')
        if s[i] != s[j]:
            res = min(res, memo(i-1, j-1) + 1)
        if l <= i and i <= r:
            res = min(res, memo(i-1, j))
        if l <= j and j <= r:
            res = min(res, memo(i, j-1))

        dp[i][j] = res
        return res

    for _ in range(q):
        l, r = map(int, input().split())
        print(memo(r, n) - memo(l-1, n))

solve()
