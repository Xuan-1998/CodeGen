import sys

def floyd_warshall(empty_cells, n, m):
    # Initialize the dp table with a large number for distances
    INF = float('inf')
    dp = [[INF if (i, j) not in empty_cells else 0 for j in range(n*m)] for i in range(n*m)]

    # Initialize distances for adjacent cells
    for cell in empty_cells:
        x, y = cell
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) in empty_cells:
                dp[x * m + y][nx * m + ny] = 1

    # Floyd-Warshall algorithm
    for k in range(n*m):
        for i in range(n*m):
            for j in range(n*m):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    # Calculate the sum of all shortest paths
    total_distance = 0
    num_paths = 0
    for i in range(n*m):
        for j in range(n*m):
            if dp[i][j] != INF and i != j:
                total_distance += dp[i][j]
                num_paths += 1

    # Calculate the average lifespan
    average_lifespan = total_distance / num_paths if num_paths else 0
    return average_lifespan

def main():
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]
    empty_cells = set()

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                empty_cells.add((i, j))

    average_lifespan = floyd_warshall(empty_cells, n, m)
    print(f"{average_lifespan:.6f}")

if __name__ == "__main__":
    main()
