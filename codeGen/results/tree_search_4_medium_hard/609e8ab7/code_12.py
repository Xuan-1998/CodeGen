def adjust_tree_values():
    n = int(input())  # Number of vertices
    parent = list(map(int, input().split()))  # Parent array
    ranges = [list(map(int, input().split())) for _ in range(n)]  # Range arrays

    dp = [[0] * (10**9 + 1) for _ in range(n + 1)]

    def dfs(i, j):
        if i == n:
            return min(0, ranges[i-1][1] - ranges[i-1][0])
        if dp[i][j]:
            return dp[i][j]
        res = float('inf')
        for k in range(max(ranges[i-1]), j+1):
            res = min(res, 1 + dfs(i-1, k))
        dp[i][j] = res
        return res

    result = []
    for i in range(1, n+1):
        result.append(dfs(i, max(map(max, [r[1] for r in ranges[:i]]))))

    print(*result, sep='\n')

adjust_tree_values()
