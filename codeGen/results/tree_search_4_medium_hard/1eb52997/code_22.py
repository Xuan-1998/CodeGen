def numMirrors(n):
    dp = [[0] * n for _ in range(n)]
    count = [n]  # Initialize with N

    for i in range(n):
        for j in range(n):
            if i > 0:  # For the first row, this condition is not necessary
                dp[i][j] = (grid[i-1][j] == '.') and all(grid[k][j] == '.' for k in range(i))
            else:
                dp[i][j] = grid[i][j] == '.'

    for i in range(n):
        for j in range(n):
            if dp[i][j]:
                count[0] -= 1
            else:
                count[0] = min(count[0], 1)
    return count[0]

T = int(input())
for _ in range(T):
    n = int(input())
    grid = [list(input()) for _ in range(n)]
    print(numMirrors(n))
