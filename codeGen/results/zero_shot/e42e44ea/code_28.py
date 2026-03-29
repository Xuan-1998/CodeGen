def main():
    N, M = map(int, input().split())
    grid = [[int(x) for x in input().split()] for _ in range(N)]
    
    min_initial_points = float('inf')
    
    for i in range(N):
        for j in range(M):
            if grid[i][j] > 0:  # Only consider cells with positive points
                initial_points = min_points(i, j)
                if initial_points < min_initial_points:
                    min_initial_points = initial_points
    
    print(min_initial_points)

if __name__ == "__main__":
    main()
