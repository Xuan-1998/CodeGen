from collections import deque

def solve():
    N = int(input())
    grid = [list(input()) for _ in range(N)]

    dp = [[0] * N for _ in range(N)]
    queue = deque()

    for j in range(N):
        if grid[0][j] == '.':
            dp[0][j] = 1
            queue.append((0, j))

    while queue:
        i, j = queue.popleft()
        for di, dj in [(-1, 0), (1, 0)]:  # up and down
            ni, nj = i + di, j + dj
            if 0 <= ni < N and grid[ni][nj] == '.':
                dp[ni][nj] = 1
                queue.append((ni, nj))

    result = sum(row.count(1) for row in dp)
    print(result)

solve()
