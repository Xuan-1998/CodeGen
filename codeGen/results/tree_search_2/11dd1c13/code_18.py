if __name__ == "__main__":
    N = int(input())
    grid = [[int(x) for x in input().split()] for _ in range(N)]
    print(min_falling_path(grid))
