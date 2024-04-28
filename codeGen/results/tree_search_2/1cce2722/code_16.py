def max_points(a):
    n = len(a)
    dp = [0] * (n + 1)

    def dfs(i, s):
        if i < 2:
            return 0
        if i > n or memo[i][s]:
            return dp[i]
        res = 0
        for j in range(1, min(n, i)):
            if a[j] == a[i-1] - 1 or a[j] == a[i-1] + 1:
                res = max(res, dfs(j-1, not s))
            else:
                res = max(res, dfs(j-1, s))
        memo[i][s] = res
        return res

    memo = [[0] * 2 for _ in range(n + 1)]
    dp[1] = 1 if a[0] != 1 else 0
    res = dfs(n - 1, True)
    return res

n = int(input())
a = list(map(int, input().split()))
print(max_points(a))
