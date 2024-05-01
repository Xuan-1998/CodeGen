n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
print(min_falling_path_sum(grid))
