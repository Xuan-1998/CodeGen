def get_min_sum(i, j):
    if (i, j) in memo:
        return memo[(i, j)]
    if i == 0 or j == 0:
        return grid[i][j]
    min_sum = min(get_min_sum(i-1, j), get_min_sum(i, j-1)) + grid[i][j]
    memo[(i, j)] = min_sum
    return min_sum

def main():
    m, n = map(int, input().split())
    global grid, memo
    grid = [list(map(int, input().split())) for _ in range(m)]
    memo = {}
    min_sum = get_min_sum(m-1, n-1)
    print(min_sum)

main()
