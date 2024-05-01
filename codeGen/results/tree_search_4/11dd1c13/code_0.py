if __name__ == '__main__':
    grid = []
    n = int(input())
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
    print(min_falling_path_sum(grid))
