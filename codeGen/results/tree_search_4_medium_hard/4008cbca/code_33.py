def min_insertions(board):
    n = len(board)
    dp = [[-1] * (n + 1) for _ in range(n + 1)]

    def dfs(i, j):
        if i >= n or j < 0:
            return -1

        if dp[i][j] != -1:
            return dp[i][j]

        if j > 0 and board[i][j - 1] == board[i][j]:
            res = min(dfs(i, j - 1), dfs(i, j + 1))
        else:
            res = dfs(i, j - 1) + 1

        dp[i][j] = res
        return res

    res = dfs(0, 0)
    if res == -1:
        print(-1, file=stdout)
    else:
        print(res, file=stdout)

min_insertions(input().strip())
