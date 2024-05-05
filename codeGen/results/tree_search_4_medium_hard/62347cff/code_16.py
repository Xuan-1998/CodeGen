m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]
print(minPathSum(grid))
