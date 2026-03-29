def min_f(n, s):
    memo = [[float('inf')] * (2*10**5 + 1) for _ in range(2*10**5 + 1)]
    memo[0][0] = 0

    def dp(i, k):
        if i == 0:
            return 0
        if k < 0 or k > s:
            return float('inf')
        if memo[i][k] != float('inf'):
            return memo[i][k]

        res = float('inf')
        for x in range(k+1):
            y = a[i-1] - x
            res = min(res, dp(i-1, k-x) + x*y)

        memo[i][k] = res
        return res

    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        print(dp(n, s))
