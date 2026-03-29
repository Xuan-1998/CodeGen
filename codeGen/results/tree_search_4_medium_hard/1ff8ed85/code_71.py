def is_possible(b):
    n = len(b)
    dp = [[False] * (n + 1) for _ in range(2)]

    def dfs(i, p):
        if i >= n:
            return all(x == 1 for x in b[:i])
        if dp[p][i]:
            return True
        res = False
        for j in range(p, -1, -1):
            if (p ^ 1) & (j | (j << 1)):
                res |= dfs(i, p ^ 1)
        dp[p][i] = res
        return res

    for i in range(n + 1):
        if dfs(i, 0) or dfs(i, 1):
            print("YES")
            return
    print("NO")


t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    is_possible(b)
