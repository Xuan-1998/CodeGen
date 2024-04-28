def numPathsWithExactlyKCoins(K, N, arr):
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    def dfs(i, j):
        if i == N - 1 and j == N - 1:
            return 1 if arr[i][j] <= K else 0
        if dp[i][j]:
            return dp[i][j]
        ways = 0
        for direction in [(i + 1, j), (i, j + 1)]:
            ni, nj = direction
            if 0 <= ni < N and 0 <= nj < N:
                remaining_coins = K - arr[ni][nj]
                ways += dfs(ni, nj)
        dp[i][j] = ways
        return ways

    return dfs(0, 0)

# Read input from stdin
K, N = map(int, input().split())
arr = [[int(x) for x in line.split()] for line in input().splitlines()]

print(numPathsWithExactlyKCoins(K, N, arr))
