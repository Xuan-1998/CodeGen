if __name__ == '__main__':
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    result = min_initial_points(grid)
    print(result)
