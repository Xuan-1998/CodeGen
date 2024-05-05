from collections import deque

def count_mirrors(N):
    grid = [list(input()) for _ in range(N)]
    
    directions = [(0, 1)]  # right
    dp = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if (i == 0 or grid[i][j] == '#') and not any((i + k, j) in directions for k in range(1, N)):
                dp[i][j] = 1
                directions.append((i, j))

    return sum(dp[-1])

T = int(input())
for _ in range(T):
    print(count_mirrors(int(input())))
