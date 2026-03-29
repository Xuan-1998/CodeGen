if __name__ == "__main__":
    M, N = map(int, input().split())
    grid = [[int(x) for x in input().split()] for _ in range(M)]
    min_points = min_initial_points(M, N, grid)
    print(min_points)
