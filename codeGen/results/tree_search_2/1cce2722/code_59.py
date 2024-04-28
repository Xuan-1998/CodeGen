def max_points(a):
    n = len(a)
    dp = [0] * (n + 1)

    def dfs(i):
        if i > n:
            return 0
        if dp[i]:
            return dp[i]

        res = 0

        for j in range(i-2, -1, -1):
            if a[j] == a[i] - 1 or a[j] == a[i] + 1:
                res += dfs(j)
                break

        dp[i] = res
        return res

    return dfs(0) + n


n = int(input())
a = list(map(int, input().split()))
print(max_points(a))
