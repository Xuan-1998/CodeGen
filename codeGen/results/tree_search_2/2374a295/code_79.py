def solve():
    n, k = map(int, input().split())
    memo = {}

    def dfs(i):
        if (i, 0) in memo:
            return memo[(i, 0)]
        if i == 1:
            return 1
        ans = 0
        for j in range(2, i+1):
            if i % j == 0:
                ans += dfs(i//j)
        memo[(i, 0)] = ans
        return ans

    print((dfs(n) - 1 + k) % 1000000007)

solve()
