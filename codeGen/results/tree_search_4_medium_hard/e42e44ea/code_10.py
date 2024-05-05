from sys import stdin

N, M = map(int, stdin.readline().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, stdin.readline().split())))

dp = [[0] * M for _ in range(N)]

def solve():
    dp[0][0] = 0
    for i in range(1, N):
        if grid[i][0] > 0:
            dp[i][0] = max(dp[i-1][0], -grid[i][0])
        else:
            break
    for j in range(1, M):
        if grid[0][j] > 0:
            dp[0][j] = max(dp[0][j-1], -grid[0][j])
        else:
            break
    for i in range(1, N):
        for j in range(1, M):
            if grid[i][j] > 0:
                dp[i][j] = max(min(dp[i-1][j], dp[i][j-1]), -grid[i][j])
            else:
                break
    return abs(dp[-1][-1])

print(solve())
