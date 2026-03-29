def dp(n, m):
    memo = {}
    def dfs(r, prev_sum):
        if (r, prev_sum) in memo:
            return memo[(r, prev_sum)]
        if r == n or prev_sum >= m:
            return 1
        total = 0
        for i in range(m + 1):
            if i <= prev_sum and i < m:
                total += dfs(r + 1, i)
        memo[(r, prev_sum)] = total % 1000000000
        return memo[(r, prev_sum)]
    return dfs(1, 0)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(dp(n, m))
