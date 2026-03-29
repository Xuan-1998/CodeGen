if __name__ == "__main__":
    m, n = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(m)]
    min_sum = min_path_sum(grid)
    print(min_sum)
