import sys

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    dp = [[0] * (1 << n) for _ in range(n)]
    f = [0]

    def gcd(x, y):
        while(y):
            x, y = y, x % y
        return x

    def solve(i, mask):
        if i < 0:
            return 0
        v = a[i]
        ans = dp[i][mask]
        for j in range(i-1, -1, -1):
            if (mask & (1 << j)) and gcd(v, a[j]) > 1:
                v = gcd(v, a[j])
                ans = max(ans, solve(j, mask ^ (1 << j)) + f[v] * v)
        return ans

    for i in range(n-1, -1, -1):
        dp[i][0] = a[i]
        for mask in range(1 << (i+1)):
            dp[i][mask] = max(dp[i][mask], solve(i, mask))
    print(dp[0][-1])

solve()
