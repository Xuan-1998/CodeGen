import sys

def f(i, j, memo):
    if i == 0:
        return grid[i][j]
    if (i, j) in memo:
        return memo[(i, j)]

    min_sum = sys.maxsize
    for k in range(i):
        min_sum = min(min_sum, f(k, j-1, memo)) + grid[i][k]

    memo[(i, j)] = min_sum
    return min_sum

def main():
    n = int(input())
    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)

    dp = {}
    min_sum = sys.maxsize
    for i in range(n):
        for j in range(len(grid[i])):
            min_sum = min(min_sum, f(i, j, dp)) + grid[i][j]

    print(min_sum)

if __name__ == "__main__":
    main()
