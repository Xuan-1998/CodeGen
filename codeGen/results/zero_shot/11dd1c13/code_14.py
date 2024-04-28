import sys
n = int(sys.stdin.readline().strip())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
min_sum = float('inf')
for j in range(n):
    temp_sum = 0
    for i in range(j+1, n):
        temp_sum += grid[i][j]
    if temp_sum < min_sum:
        min_sum = temp_sum
print(min_sum)
