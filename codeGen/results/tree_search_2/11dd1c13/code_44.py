import sys

def min_falling_path_sum(grid):
    n = len(grid)
    memo = [[0] * len(grid[0]) for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(len(grid[0])):
            if i == n - 1:
                memo[i][j] = grid[i][j]
            else:
                min_val = sys.maxsize
                for k in range(len(grid[0])):
                    if k != j and (i + 1 < n or k > j):
                        min_val = min(min_val, memo[i + 1][k])
                memo[i][j] = grid[i][j] + min_val

    return min(memo[0])

def main():
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    print(min_falling_path_sum(grid))

if __name__ == "__main__":
    main()
