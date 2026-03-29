def solve(t, s):
    n = len(s)
    dp = [float('inf')] * (len(t) + 1)
    dp[0] = 0

    memo = {}

    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i >= len(t):
            return float('inf')

        if j > n or dp[i] == -1:
            return dp[i]

        res = min(dfs(i + 1, j) + 1, dfs(i + 1, j) if s[j - 1].strip() not in t[:i] else dfs(i + len(s[j - 1]), j - 1))

        memo[(i, j)] = res
        return res

    m = dfs(0, n)
    if m == float('inf'):
        print(-1)
    else:
        for i in range(m):
            idx = t.find(s[i % n])
            print(i, idx)
        print(m)

input()
while True:
    try:
        t = input().strip()
        n = int(input())
        s = [input().strip() for _ in range(n)]
        solve(t, s)
    except:
        break
