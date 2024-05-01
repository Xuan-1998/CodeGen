from collections import deque

def min_tiles(n, m):
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    dq = deque([(n, m, 0)])  # (i, j, min_tiles)

    while dq:
        i, j, min_tiles = dq.popleft()
        if i == 0 or j == 0:  # base case
            continue

        for size in range(1, min(i, j) + 1):
            ni, nj = i - size, j - size
            dp[i][j] = min(dp[i][j], dp[ni][nj] + (size ** 2))

        if i > 0:  # add top cells to queue
            dq.append((i - 1, j, dp[i-1][j]))
        if j > 0:  # add left cells to queue
            dq.append((i, j - 1, dp[i][j-1]))

    return dp[-1][-1]

# Example usage:
n, m = map(int, input().split())
print(min_tiles(n, m))
