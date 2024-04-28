def max_points(a):
    n = len(a)
    dp = [0] * (n + 1)

    def dfs(s):
        if s <= 1:
            return 0
        if dp[s] > 0:
            return dp[s]
        res = 0
        if a[s - 1] == s:
            res = max(res, dfs(s - 2) + s)
        else:
            res = max(res, dfs(s - 1) + 1)
        dp[s] = res
        return res

    return dfs(n)

n = int(input())
a = [int(x) for x in input().split()]
print(max_points(a))
