def find_distinct_sums():
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [[False] * (sum(arr) + 1) for _ in range(n + 1)]
    sums = set()

    def dfs(i, j):
        if j < 0:
            return False
        if j == 0:
            return True
        if i > n or dp[i][j]:
            return dp[i][j]
        dp[i][j] = (arr[i - 1] <= j) and (dfs(i - 1, j - arr[i - 1]) or dfs(i - 1, j))
        return dp[i][j]

    for i in range(1, n + 1):
        for j in range(sum(arr) + 1):
            if dfs(i, j):
                sums.add(j)

    print(' '.join(map(str, sorted(list(sums)))))
