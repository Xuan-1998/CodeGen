def simulate_program(a):
    n = len(a) + 1
    dp = [[-1, False] for _ in range(n)]

    def dfs(x, y):
        if x <= 0 or x > n:
            return y
        if not dp[x][1]:
            new_x = max(2, x)
            new_y = y + a[x]
            dp[new_x][0], dp[new_x][1] = dfs(new_x, new_y), True
            new_x = new_x - a[x]
            new_y = new_y + a[x]
            if new_x > n or new_x <= 0:
                return new_y
            dp[new_x][0], dp[new_x][1] = dfs(new_x, new_y), True
        return dp[x][0]

    for i in range(2, n+1):
        print(dfs(i, 0))

