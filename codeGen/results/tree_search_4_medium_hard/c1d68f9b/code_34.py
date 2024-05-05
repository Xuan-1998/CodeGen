def can_form_polygon(n, moods):
    if n < 3:
        return "NO"

    good_moods = sum(moods)
    bad_moods = n - good_moods

    memo = {}

    def dfs(i, k):
        if (i, k) in memo:
            return memo[(i, k)]

        res = False
        for j in range(i-1, -1, -1):
            if moods[j] == moods[i]:
                res = True
                break

        if res:
            dp[i][k] = dfs(i-1, k)
        else:
            dp[i][k] = (dp[i-1][k-1]) or dfs(i-1, k)

        memo[(i, k)] = dp[i][k]

        return dp[i][k]

    res = True
    for i in range(n):
        if moods[i]:
            res &= dfs(i, 0)
        else:
            res &= dfs(i, 1)

    if good_moods > n // 2 or bad_moods > n // 2:
        return "NO"
    return "YES" if res else "NO"

n = int(input())
moods = list(map(int, input().split()))
print(can_form_polygon(n, moods))
