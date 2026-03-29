def is_ladder(arr, queries):
    n = len(arr)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    last_non_decreasing_element = [[-1] * (n + 1) for _ in range(n + 1)]

    def dfs(i, j):
        if i > j:
            return 0
        if dp[i][j] != 0:
            return dp[i][j]
        if arr[j] <= last_non_decreasing_element[i][j - 1]:
            dp[i][j] = 1 + dfs(i, j - 1)
        else:
            dp[i][j] = max(dfs(i, j - 1), dfs(i, j))
        return dp[i][j]

    for query in queries:
        l, r = query
        if arr[r] <= last_non_decreasing_element[l][r]:
            print("Yes")
        else:
            print("No")

    return

# Example usage:
arr = [4, 2, 3, 1, 5]
queries = [[0, 4], [1, 3]]
is_ladder(arr, queries)
